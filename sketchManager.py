import sys

sys.path.append('C:\Program Files\FreeCAD 0.16')

import FreeCAD
import FreeCADGui
from PySide import QtGui
import Sketcher
import Draft, Part

App = FreeCAD
Gui = FreeCADGui


def clearPythonSession():
    import sys
    # print sys.modules
    # for i in sys.modules:
    #	print i
    toReload = ['libfunc.mathfuncs', 'pointclass', 'lineclass', 'circleclass', 'sketchManager', 'patterns', 'libfunc',
                'v2d', 'constraints', 'shapes']

    for s in toReload:
        if s in sys.modules:
            sys.modules['conCAD'].__dict__.clear()
    import FreeCAD


runOnce = True


def createSketchIfNoneExist():
    FreeCADGui.activateWorkbench("SketcherWorkbench")

    if App.activeDocument() is None:
        App.newDocument("Unnamed")
        FreeCAD.setActiveDocument("Unnamed")

    # print "clearing sketch"
    try:
        FreeCAD.activeDocument().removeObject('Sketch')
    except:
        pass
    FreeCAD.activeDocument().addObject('Sketcher::SketchObject', 'Sketch')
    FreeCADGui.activeDocument().setEdit('Sketch')
    FreeCADGui.activeDocument().activeView().setCamera(
        '#Inventor V2.1 ascii \n OrthographicCamera {\n viewportMapping ADJUST_CAMERA \n position 0 0 87 \n orientation 0 0 1  0 \n nearDistance -112.88701 \n farDistance 287.28702 \n aspectRatio 1 \n focalDistance 87 \n height 143.52005 }')

    # global runOnce
    # if runOnce:


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


def sketchGeometry(index):
    return App.ActiveDocument.Sketch.Geometry[index]


def sketchConstraints():
    return App.ActiveDocument.Sketch.Constraints


def sketchConstraint(index):
    return App.ActiveDocument.Sketch.Constraints[index]


def clearAll():
    doc = App.ActiveDocument
    for obj in doc.Objects:
        doc.removeObject(obj.Label)


def last():
    return App.ActiveDocument.Sketch.GeometryCount - 1


def sk():
    return App.ActiveDocument.Sketch


def display():
    App.activeDocument().recompute()
    Gui.SendMsgToActiveView("ViewFit")
