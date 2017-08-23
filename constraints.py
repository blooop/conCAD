from sketchManager import *
import Sketcher

def conDis(dis, obj=None):
    sk().addConstraint(Sketcher.Constraint('Distance', obj, dis))

# def constrainDistance(dis, obj1,obj2):
#     if isinstance(obj,pt):
#         sk().addConstraint(Sketcher.Constraint('Distance', obj.id, dis))
#     elif isinstance(obj,ln):
#         sk().addConstraint(Sketcher.Constraint('Distance', obj.id, dis))


def conRad(rad, obj=None):
    if obj is None:
        obj = last()

    sk().addConstraint(Sketcher.Constraint('Radius', obj, rad))

def conDisAxis(dis, axis1, axis2, atMidPoints=False):
    ln = line(construction=True)
    conDis(dis)

    if atMidPoints:
        md1 = midPoint(axis1)
        conCoince(ln, md1, 1, 1)
        md2 = midPoint(axis2)
        conCoince(ln, md2, 2, 1)
    else:
        conPointOnCurve(last(), 1, axis1)
        conPointOnCurve(last(), 2, axis2)
    conPerp(ln, axis1)
    conPerp(ln, axis2)

def conEq(obj1=None, obj2=None):
    if obj1 is None:
        obj1 = last() - 1
    if obj2 is None:
        obj2 = last()
    sk().addConstraint(Sketcher.Constraint('Equal', obj1, obj2))


def conCoince(obj1=None, obj2=None, obj1Side=2, obj2side=1):
    print obj1, obj2, obj1Side, obj2side
    if obj1 is None:
        obj1 = last() - 1
    if obj2 is None:
        obj2 = last()
    print "coincident between: ", obj1, " ", obj2
    sk().addConstraint(Sketcher.Constraint('Coincident', obj1, obj1Side, obj2, obj2side))


def conPerp(line1, line2):
    sk().addConstraint(Sketcher.Constraint('Perpendicular', line1, line2))


def conPointOnCurve(linePoint, pointSide, curve):
    sk().addConstraint(Sketcher.Constraint('PointOnObject', linePoint, pointSide, curve))


def midPoint(line):
    point()
    conSym(line, START, line, END, last(), START)


def conVert(obj1=None, obj2=None):
    if obj1 is None:
        obj1 = last() - 1
    if obj2 is None:
        obj2 = last()
    sk().addConstraint(Sketcher.Constraint('DistanceX', obj1, 3, obj2, 3))


def conPara(line1, line2):
    sk().addConstraint(Sketcher.Constraint('Parallel', line1, line2))


def conSym(obj1, obj1Side, obj2, obj2Side, symAbout, symAboutSide=None):
    sk().addConstraint(Sketcher.Constraint('Symmetric', obj1, obj1Side, obj2, obj2Side, symAbout, symAboutSide))


def conSymAxis(obj1, obj1Side, obj2, obj2Side, symAbout):
    sk().addConstraint(Sketcher.Constraint('Symmetric', obj1, obj1Side, obj2, obj2Side, symAbout))


def symmetric(objects, axis):
    return 1