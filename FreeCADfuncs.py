import sys
sys.path.append('C:\Program Files\FreeCAD 0.16')
sys.path.append('D:\Dropbox\src\FreeCAD\conCAD')
import FreeCAD

App = FreeCAD
import FreeCADGui
Gui = FreeCADGui
import Sketcher
import Draft, Part
from FreeCAD import Gui
import random
from PySide import QtGui
import math
import collections

#from circle import *
#from constraints import *
#import patterns

lines = dict()
loops = []

PI = math.pi
PI2 = math.pi * 2.0
PIB2 = math.pi / 2.0

class circle:
    def __init__(self,rad,pos=None,construction=False):
        self.rad = rad
        self.pos = pos or pt()
        # sk().addGeometry(Part.Circle(pos,App.Vector(0, 0, 1), rad),construction=construction)
        self.id = sk().addGeometry(Part.Circle(),construction)
        conRad(self.rad,self.id)
        # if pos is not None:

    def conPoint(self,pnt):
        sk().addConstraint(Sketcher.Constraint('Coincident',self.id,3,pnt.id,1))

    def conDis(self,obj,dis):
        conDis(dis,obj)

def conRad(rad, obj=None):
    if obj is None:
        obj = last()

    sk().addConstraint(Sketcher.Constraint('Radius', obj, rad))

def a2v(angle):
    return v(math.cos(angle), math.sin(angle))

def lerp(value, inputLow, inputHigh, outputLow, outputHigh):
    return outputLow + ((value - inputLow) / (inputHigh - inputLow)) * (outputHigh - outputLow)

def clearConsole():
    mw = Gui.getMainWindow()
    c = mw.findChild(QtGui.QPlainTextEdit, "Python console")
    c.clear()
    r = mw.findChild(QtGui.QTextEdit, "Report view")
    r.clear()

def delGeometry(index):
    App.ActiveDocument.Sketch.delGeometry(index)

def clearAll():
    doc = App.ActiveDocument
    for obj in doc.Objects:
        doc.removeObject(obj.Label)

def randVec(instances=1):
    if instances > 1:
        output = []
        for i in range(instances):
            output.append(v(random.random(), random.random()))
        return output
    return v(random.random(), random.random())

def v(x=0, y=0):
    return App.Vector(x, y, 0)

def last():
    return App.ActiveDocument.Sketch.GeometryCount - 1

def sk():
    return App.ActiveDocument.Sketch

def init():
    App.setActiveDocument("Unnamed")
    App.ActiveDocument = App.getDocument("Unnamed")
    Gui.ActiveDocument = Gui.getDocument("Unnamed")
    Gui.activateWorkbench("SketcherWorkbench")
    App.activeDocument().addObject('Sketcher::SketchObject', 'Sketch')
    App.activeDocument().Sketch.Placement = App.Placement(App.Vector(0.000000, 0.000000, 0.000000),
                                                           App.Rotation(0.000000, 0.000000, 0.000000, 1.000000))
    Gui.activeDocument().activeView().setCamera('#Inventor V2.1 ascii \n OrthographicCamera {\n viewportMapping ADJUST_CAMERA \n position 0 0 87 \n orientation 0 0 1  0 \n nearDistance -112.88701 \n farDistance 287.28702 \n aspectRatio 1 \n focalDistance 87 \n height 143.52005 }')
    Gui.activeDocument().setEdit('Sketch')

def clearConsole():
    mw = Gui.getMainWindow()
    c = mw.findChild(QtGui.QPlainTextEdit, "Python console")
    c.clear()
    r = mw.findChild(QtGui.QTextEdit, "Report view")
    r.clear()

def clearDoc():
    for i in range(App.ActiveDocument.Sketch.ConstraintCount - 1, -1, -1):
        App.ActiveDocument.Sketch.delConstraint(i)

    for i in range(App.ActiveDocument.Sketch.GeometryCount - 1, -1, -1):
        App.ActiveDocument.Sketch.delGeometry(i)


def delGeometry(index):
    App.ActiveDocument.Sketch.delGeometry(index)


def clearAll():
    doc = App.ActiveDocument
    for obj in doc.Objects:
        doc.removeObject(obj.Label)


def CreateCircleSketch(SketchFeature, center, radius):
    i = int(SketchFeature.GeometryCount)
    SketchFeature.addGeometry(Part.Circle(App.Vector(*center), App.Vector(0, 0, 1), radius), False)
    SketchFeature.addConstraint(Sketcher.Constraint('Radius', i, radius))

def randVec(instances=1):
    if instances > 1:
        output = []
        for i in range(instances):
            output.append(v(random.random(), random.random()))
        return output
    return v(random.random(), random.random())


def v(x=0, y=0):
    return App.Vector(x, y, 0)

def defineOriginPt():
    origin = pt(defineOrigin = True)
    origin.id = -1

    horAxis = ln(defineOrigin=True)
    horAxis.id = -1

    vertAxis = ln(defineOrigin=True)
    vertAxis.id = -2

    return origin,horAxis,vertAxis

class pt:
    def __init__(self, pos=None,defineOrigin = False):
        if not defineOrigin:
            self.pos = pos or v()
            self.id = sk().addGeometry(Part.Point(self.pos))

    def origin(self):
        self.pos = v(0, 0)
        self.id = -1

    def conPoint(self, pnt):
        otherid = 1
        if isinstance(pnt,circle):
            otherid = 3
        sk().addConstraint(Sketcher.Constraint('Coincident', self.id, 1, pnt.id, otherid))

    def lineTo(self, otherPoint=None, dis=None):
        tmp = ln(self, otherPoint, dis)
        return tmp

    def conVert(self,point):
        ln(self,point,construction=True).conVert()

    def conDis(self,point,dis):
        conId = sk().addConstraint(Sketcher.Constraint('Distance',  self.id,1,point.id,1, dis))
        sk().setDatum(conId,App.Units.Quantity(str(dis) +' mm'))

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

class ln:
    def __init__(self, start=None, end=None, dis=None, construction=False,defineOrigin = False):
        if not defineOrigin:
            self.start = start or pt()
            self.end = end or pt()
            self.id = line(construction=construction)
            self._midpoint = None

            if dis is not None:
                self.setLen(dis)

            sk().addConstraint(Sketcher.Constraint('Coincident', self.start.id, 1, self.id, 1))
            sk().addConstraint(Sketcher.Constraint('Coincident', self.end.id, 1, self.id, 2))

    def midpoint(self):
        if self._midpoint is None:
            self._midpoint = pt()
            sk().addConstraint(Sketcher.Constraint('Symmetric', self.start.id, 1, self.end.id, 1, self._midpoint.id, 1))
        return self._midpoint

    def conLen(self, dis):
        if dis is not None:
            conDis(dis, self.id)
        else:
            print "cannot constrain length to None"

    def perp(self, line1):
        conPerp(self.id, line1.id)

    def conHor(self):
        sk().addConstraint(Sketcher.Constraint('Horizontal', self.id))

    def conVert(self):
        sk().addConstraint(Sketcher.Constraint('Vertical', self.id))

    def conAng(self, line1,angle):
        tmp = sk().addConstraint(Sketcher.Constraint('Angle',self.id,1,line1.id,1,angle))
        sk().setDatum(tmp, App.Units.Quantity(str(angle)+' deg'))

    def conEq(self,line1):
        sk().addConstraint(Sketcher.Constraint('Equal', self.id, line1.id))


def line(start=None, end=None, construction=False, name=None):
    if start is None:
        start = randVec()
    if end is None:
        end = randVec()
    id = sk().addGeometry(Part.Line(start, end), construction)
    if name is not None:
        lines[name] = id
    return last()

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


def conDis(dis, obj):
    if isinstance(obj,pt):
        sk().addConstraint(Sketcher.Constraint('Distance', obj, dis))
    elif isinstance(obj,ln):
        sk().addConstraint(Sketcher.Constraint('Distance', obj, dis))

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

def symmetric(objects,axis):
    return 1

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
