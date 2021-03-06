from sketchManager import *

import collections

from v2d import *

import pointclass
import nodeclass
import cons
import circleclass

import Sketcher

lines = dict()
loops = []


class ln(nodeclass.Node):
    def __init__(self, start=None, end=None, dis=None, construction=False, defineOrigin=False):
        super(ln, self).__init__()

        if not defineOrigin:

            if isinstance(start,App.Vector):
                startVec = start
                self.start = None
            else:
                startVec = v(0, 0)
                self.start = start

            if isinstance(end, App.Vector):
                endVec = end
                self.end = None
            else:
                endVec = v(0, 0)
                self.end = end

            self.id = sk().addGeometry(Part.Line(startVec, endVec), construction)

            if self.start is None:
                self.start = pointclass.pt.lineStart(self)
            cons.PointOnLine(self.start, self, 1)

            if self.end is  None:
                self.end = pointclass.pt.lineEnd(self)
            cons.PointOnLine(self.end, self, 2)

            if dis is not None:
                self.conLen(dis)

    def subTraverse(self, result):
        result.lines.append(self)

        if not ln in result.all:
            result.all[ln] = set()
        result.all[ln].add(self)


    def midpoint(self):
        if self._midpoint is None:
            self._midpoint = pointclass.pt()
            sk().addConstraint(Sketcher.Constraint('Symmetric', self.start.id, 1, self.end.id, 1, self._midpoint.id, 1))
        return self._midpoint

    def conLen(self, dis):
        if dis is not None:
            sk().addConstraint(Sketcher.Constraint('Distance', self.id, dis))
        else:
            print "cannot constrain length to None"

    def perp(self, line1):
        sk().addConstraint(Sketcher.Constraint('Perpendicular', self.id, line1.id))

    def conHor(self):
        sk().addConstraint(Sketcher.Constraint('Horizontal', self.id))

    def conVert(self):
        sk().addConstraint(Sketcher.Constraint('Vertical', self.id))

    def conAng(self, line1, angle):
        tmp = sk().addConstraint(Sketcher.Constraint('Angle', self.id, 1, line1.id, 1, angle))
        sk().setDatum(tmp, App.Units.Quantity(str(angle) + ' deg'))

    def conEq(self, line1):
        sk().addConstraint(Sketcher.Constraint('Equal', self.id, line1.id))

    def __str__(self):
        return "ln:" + str(self.id)


def polyLine(pointsList, distances=None, angles=None, closeLoop=False, construction=False):
    lines = []

    if closeLoop:
        start = -1
    else:
        start = 0

    iterator = range(start, len(pointsList) - 1)

    for i in iterator:
        lines.append(ln(pointsList[i], pointsList[i + 1]))

    for i in iterator:
        cons.PointOnPoint(lines[i].end,lines[i+1].start)

    if distances is not None:
        distanceDict = dict()

        distances = makeSureIsList(distances, len(lines))

        for i in range(0, len(distances)):
            if not distances[i] in distanceDict:
                distanceDict[distances[i]] = [i]
            else:
                distanceDict[distances[i]].append(i)
        #print distanceDict
        for key, value in distanceDict.iteritems():
            if key is not None:
                lines[value[0]].conLen(key)
                if len(value) > 1:
                    for i in range(1, len(value)):
                        lines[value[0]].conEq(lines[value[i]])

    if angles is not None:
        angles = makeSureIsList(angles, len(pointsList))
        for i in iterator:
            lines[i].conAng(lines[i + 1], angles[i])

    return lines


def loop(num, distances=None, angles=None, closed=True, construction=False):
    points = []
    if not closed:
        num += 1
    for i in range(num):
        ang = PIB2 + lerp(i, 0.0, num, 0.0, PI2)
        points.append(a2v(ang))
    loops.append(polyLine(points, distances, angles=angles, closeLoop=closed, construction=False))
    return loops[-1]


def makeSureIsList(candidate, desiredLen):
    if not isinstance(candidate, collections.Iterable):
        candidate = [candidate] * desiredLen
    return candidate


def defineDatumAxes():
    horAxis = ln(defineOrigin=True)
    horAxis.id = -1

    vertAxis = ln(defineOrigin=True)
    vertAxis.id = -2
    return horAxis, vertAxis


[horAxis, vertAxis] = defineDatumAxes()
