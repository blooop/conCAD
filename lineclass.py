from sketchManager import *
from cons import *

import collections

from v2d import *

import pointclass
from itemclass import *
import circleclass
import Sketcher

lines = dict()
loops = []

class ln(baseitem):
    def __init__(self, start=None, end=None, dis=None, construction=False, defineOrigin=False):
        #baseitem.__init__(self)
        #print baseitem.globalCounter
        #print baseitem.i
        #print self.uniqueID
        #print 2

        if not defineOrigin:
            self.start = start or pointclass.pt()
            self.end = end or pointclass.pt(v(1,0))
            self.id = sk().addGeometry(Part.Line(), construction)
            self._midpoint = None

            if dis is not None:
                self.conLen(dis)

            #self.nodes.append(self.start)
            sk().addConstraint(Sketcher.Constraint('Coincident', self.start.id, 1, self.id, 1))
            #self.start.nodes
            #self.nodes.append(self.end)
            sk().addConstraint(Sketcher.Constraint('Coincident', self.end.id, 1, self.id, 2))

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


def polyLine(pointsList, distances=None, angles=None, closeLoop=False, construction=False):
    lineIndices = []
    lineIndices.append(ln(pointsList[0], pointsList[1], construction=construction))

    for i in range(2, len(pointsList)):
        lineIndices.append(lineIndices[-1].end.lineTo(pointsList[i]))
    if closeLoop:
        lineIndices.append(lineIndices[-1].end.lineTo(lineIndices[0].start))

    if distances is not None:
        distanceDict = dict()

        if not isinstance(distances, collections.Iterable):
            distanceDict[distances] = range(len(lineIndices))
            lineIndices[0].conLen(distances)
            for i in range(1, len(lineIndices)):
                lineIndices[0].conEq(lineIndices[i])
        else:
            for i in range(len(distances)):
                if not distances[i] in distanceDict:
                    distanceDict[distances[i]] = [i]
                else:
                    distanceDict[distances[i]].append(i)

        for key, value in distanceDict.iteritems():
            if len(value) > 1:
                lineIndices[value[0]].conLen(key)
                for i in range(1, len(value)):
                    lineIndices[value[0]].conEq(lineIndices[value[i]])
            else:
                lineIndices[value[0]].conLen(key)

    if angles is not None:
        angles = makeSureIsList(angles, len(pointsList))
        for i in range(len(lineIndices) - 1):
            lineIndices[i].conAng(lineIndices[i + 1], angles[i])

    return lineIndices


def makeSureIsList(candidate, desiredLen):
    if not isinstance(candidate, collections.Iterable):
        candidate = [candidate] * desiredLen
    return candidate


def loop(num, distances=None, angles=None, closed=True, construction=False):
    points = []
    if not closed:
        num += 1
    for i in range(num):
        points.append(pointclass.pt(a2v(PIB2 + lerp(i, 0.0, num, 0.0, PI2))))
    loops.append(polyLine(points, distances, angles=angles, closeLoop=closed, construction=False))
    return loops[-1]


def defineDatumAxes():
    horAxis = ln(defineOrigin=True)
    horAxis.id = -1

    vertAxis = ln(defineOrigin=True)
    vertAxis.id = -2
    return horAxis, vertAxis


[horAxis, vertAxis] = defineDatumAxes()
