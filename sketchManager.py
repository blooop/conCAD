import sys
sys.path.append('C:\Program Files\FreeCAD 0.16')

import FreeCAD
import FreeCADGui



def createSketchIfNoneExist():
    FreeCADGui.activateWorkbench("SketcherWorkbench")
    #if App.activeDocument() is None:
    #App.newDocument("Unnamed")
    FreeCAD.setActiveDocument("Unnamed")
    FreeCAD.activeDocument().addObject('Sketcher::SketchObject', 'Sketch')
    FreeCADGui.activeDocument().setEdit('Sketch')
    FreeCADGui.activeDocument().activeView().setCamera('#Inventor V2.1 ascii \n OrthographicCamera {\n viewportMapping ADJUST_CAMERA \n position 0 0 87 \n orientation 0 0 1  0 \n nearDistance -112.88701 \n farDistance 287.28702 \n aspectRatio 1 \n focalDistance 87 \n height 143.52005 }')
