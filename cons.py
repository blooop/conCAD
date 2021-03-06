from sketchManager import *
import Sketcher

import nodeclass


class Constraint(nodeclass.Node):
    def __init__(self):
        super(Constraint, self).__init__()

    def subTraverse(self, result):
        result.constraints.append(self)


class PointOnPoint(Constraint):
    def __init__(self, point1, point2):
        super(PointOnPoint, self).__init__()
        sk().addConstraint(Sketcher.Constraint('Coincident', point1.id, point1.pntType, point2.id, point2.pntType))
        self.link(point1)
        self.link(point2)


class PointOnLine(Constraint):
    def __init__(self, point1, line1,lineStartOrEnd):
        super(PointOnLine, self).__init__()
        #sk().addConstraint(Sketcher.Constraint('Coincident', line1.id, lineStartOrEnd, point1.id, point1.pntType))
        self.link(point1)
        self.link(line1)

    def __str__(self):
        return "pointOnPoint" + str(id)

class LineOnPoint(Constraint):
    def __init__(self, line1, point1, lineStartOrEnd):
        super(LineOnPoint, self).__init__()
        #self.id = sk().addConstraint(Sketcher.Constraint('Coincident', point1.id, point1.pntType, line1.id, lineStartOrEnd))
        self.link(line1)
        self.link(point1)


def point2point(p1, p2):
    sk().addConstraint(Sketcher.Constraint('Coincident', p1.id, 1, p2.id, 1))


def lineStartToPoint(linestart, point):
    sk().addConstraint(Sketcher.Constraint('Coincident', linestart.id, 1, point, 1))
    linestart.nodes.append()


    #
    # def conDis(dis, obj=None):
    #     sk().addConstraint(Sketcher.Constraint('Distance', obj, dis))
    #
    # # def constrainDistance(dis, obj1,obj2):
    # #     if isinstance(obj,pt):
    # #         sk().addConstraint(Sketcher.Constraint('Distance', obj.id, dis))
    # #     elif isinstance(obj,ln):
    # #         sk().addConstraint(Sketcher.Constraint('Distance', obj.id, dis))
    #
    #
    # def conRad(rad, obj=None):
    #     if obj is None:
    #         obj = last()
    #
    #     sk().addConstraint(Sketcher.Constraint('Radius', obj, rad))
    #
    # def conDisAxis(dis, axis1, axis2, atMidPoints=False):
    #     ln = line(construction=True)
    #     conDis(dis)
    #
    #     if atMidPoints:
    #         md1 = midPoint(axis1)
    #         conCoince(ln, md1, 1, 1)
    #         md2 = midPoint(axis2)
    #         conCoince(ln, md2, 2, 1)
    #     else:
    #         conPointOnCurve(last(), 1, axis1)
    #         conPointOnCurve(last(), 2, axis2)
    #     conPerp(ln, axis1)
    #     conPerp(ln, axis2)
    #
    # def conEq(obj1=None, obj2=None):
    #     if obj1 is None:
    #         obj1 = last() - 1
    #     if obj2 is None:
    #         obj2 = last()
    #     sk().addConstraint(Sketcher.Constraint('Equal', obj1, obj2))
    #
    #
    # def conCoince(obj1=None, obj2=None, obj1Side=2, obj2side=1):
    #     print obj1, obj2, obj1Side, obj2side
    #     if obj1 is None:
    #         obj1 = last() - 1
    #     if obj2 is None:
    #         obj2 = last()
    #     print "coincident between: ", obj1, " ", obj2
    #     sk().addConstraint(Sketcher.Constraint('Coincident', obj1, obj1Side, obj2, obj2side))
    #
    #
    # def conPerp(line1, line2):
    #     sk().addConstraint(Sketcher.Constraint('Perpendicular', line1, line2))
    #
    #
    # def conPointOnCurve(linePoint, pointSide, curve):
    #     sk().addConstraint(Sketcher.Constraint('PointOnObject', linePoint, pointSide, curve))
    #
    #
    # def midPoint(line):
    #     point()
    #     conSym(line, START, line, END, last(), START)
    #
    #
    # def conVert(obj1=None, obj2=None):
    #     if obj1 is None:
    #         obj1 = last() - 1
    #     if obj2 is None:
    #         obj2 = last()
    #     sk().addConstraint(Sketcher.Constraint('DistanceX', obj1, 3, obj2, 3))
    #
    #
    # def conPara(line1, line2):
    #     sk().addConstraint(Sketcher.Constraint('Parallel', line1, line2))
    #
    #
    # def conSym(obj1, obj1Side, obj2, obj2Side, symAbout, symAboutSide=None):
    #     sk().addConstraint(Sketcher.Constraint('Symmetric', obj1, obj1Side, obj2, obj2Side, symAbout, symAboutSide))
    #
    #
    # def conSymAxis(obj1, obj1Side, obj2, obj2Side, symAbout):
    #     sk().addConstraint(Sketcher.Constraint('Symmetric', obj1, obj1Side, obj2, obj2Side, symAbout))
    #
    #
    # def symmetric(objects, axis):
    #     return 1
