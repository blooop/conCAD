#from conCAD import *

import collections

from libfunc.mathfuncs import *
from sketchManager import *
from v2d import *
from constraints import *
from pt import pt
from ln import ln
from circle import circle

#from constraints import *
#import patterns

lines = dict()
loops = []

def pattern(obj,vector,instances):
    output = []

    baseConstruction = ln(dis =vecLen(vector))
    construction = [baseConstruction]
    # ln1 = ln(dis=2)
    # ln1.start.conPoint(origin)
    # ln1.conAng(horAxis, 0.3)
    # for obj in objList:
    vlen = vecLen(vector)
    if isinstance(obj,circle):
        obj.conPoint(baseConstruction.start)
        print v2ad(vector)
        baseConstruction.conAng(horAxis,v2ad(vector))

        for i in range(instances-1):
        #
            tmpln = ln(construction[-1].end,construction=True )
            construction[-1].conAng(tmpln,0)
            output.append(circle(tmpln.start))
            tmpln.conEq(baseConstruction)
            construction.append(tmpln)

        # output[-1]

def defineOriginPt():
    origin = pt(defineOrigin = True)
    origin.id = -1

    horAxis = ln(defineOrigin=True)
    horAxis.id = -1

    vertAxis = ln(defineOrigin=True)
    vertAxis.id = -2

    return origin,horAxis,vertAxis

def point(coords=None):
    if coords is None:
        coords = v()
    return sk().addGeometry(Part.Point(coords))

def polyLine(pointsList,distances=None,angles= None, closeLoop=False, construction=False):
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
            for i in range(1,len(lineIndices)):
                lineIndices[0].conEq(lineIndices[i])
        else:
            for i in range(len(distances)):
                if not distances[i] in distanceDict:
                    distanceDict[distances[i]] = [i]
                else:
                    distanceDict[distances[i]].append(i)

        for key, value in distanceDict.iteritems():
            if len(value) >1:
                lineIndices[value[0]].conLen(key)
                for i in range(1,len(value)):
                    lineIndices[value[0]].conEq(lineIndices[value[i]])
            else:
                lineIndices[value[0]].conLen(key)

    if angles is not None:
        angles = makeSureIsList(angles, len(pointsList))
        for i in range(len(lineIndices)-1):
            lineIndices[i].conAng(lineIndices[i+1], angles[i])

    return lineIndices

def applyProperty(objects,propertyItemOrList,func):
    propertyItemOrList = makeSureIsList(propertyItemOrList, len(objects))
    if propertyItemOrList is not None:
        for i in range(len(objects)):
            objects[i] = func(objects[i],propertyItemOrList[i])
    return objects

def makeSureIsList(candidate,desiredLen):
    if not isinstance(candidate, collections.Iterable):
        candidate = [candidate]* desiredLen
    return candidate

def loop(num,distances = None,angles = None, closed=True, construction=False):
    points = []
    if not closed:
        num+=1
    for i in range(num):
        points.append(pt(a2v(PIB2 + lerp(i, 0.0, num, 0.0, PI2))))
    loops.append(polyLine(points,distances,angles = angles, closeLoop=closed, construction=False))
    return loops[-1]



def fillet(rad, obj1=None, obj2=None):
    if obj1 is None:
        obj1 = last() - 1
    if obj2 is None:
        obj2 = last()
    sk().fillet(obj1, obj2, rad)


def filletTri(sideLen):
    line(v(0, 1), v(2, 3))
    conDis(100)
    conHor()
    line(v(2, 3), v(5, 6))
    conEq()
    conCoince()
    line(v(5, 6), v(8, 9))
    conEq()
    conCoince()
    conCoince(0, last(), 1, 2)

    fillets = []
    fillet(10.0, 0, 1)
    fillets.append(last())
    conRad(sideLen / 5.0)
    fillet(10.0, 0, 2)
    fillets.append(last())
    # App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Radius',App.ActiveDocument.Sketch.GeometryCount-1,10))
    fillet(10.0, 1, 2)
    fillets.append(last())
    for i in range(len(fillets) - 1):
        sk().addConstraint(Sketcher.Constraint('Equal', fillets[i], fillets[i + 1]))
    conCoince(-1, 5, 1, 3)
    conDis(sideLen, 0)


def display():
    App.activeDocument().recompute()
    Gui.SendMsgToActiveView("ViewFit")


def antenna():
    spoke = ln(dis=2)
    rim = ln(dis=1)

    spoke.start.conPoint(origin)
    spoke.end.conPoint(rim.midpoint())
    spoke.perp(rim)

    ln1 = rim.start.lineTo(dis=1.5)
    ln2 = rim.end.lineTo(dis=1.5)
    ln1.end.conPoint(ln2.end)


def trapezoid(parralelDis, leftLen, rightLen, isosolese=True):
    [top, right, bottom, left] = loop(4)
    conPara(top, bottom)
    #	conDis(leftLen,left)
    #	conDis(rightLen,right)
    if isosolese:
        ln1 = line()
        conCoince(ln1, bottom, 2, 1)
        ln2 = line()
        conCoince(ln2, bottom, 2, 2)
        conCoince(ln1, ln2, 1, 1)
        md = midPoint(top)
        #		conEq(ln1,ln2)
        #		conCoince(ln1,md,1)
        #		conPara(ln1,right)
        #		conPara(ln2,left)
        conEq(left, right)

    return [top, right, bottom, left]


# trapezoid(5,1,2)

def trapOld():
    linkLen = 5
    leftRad = 1
    rightRad = leftRad * 2
    [top, right, bottom, left] = loop(4)
    print top
    conSymAxis(top, 2, bottom, 1, -1)
    # conSymAxis(top,1,bottom,2,-1)
    conDis(leftRad, left)
    conDis(rightRad, right)
    conDisAxis(linkLen, right, left, True)



[origin,horAxis,vertAxis] = defineOriginPt()