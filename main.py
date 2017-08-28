# from conCAD import *
from libfunc.util.IO import *

# fileList = glob.glob("*.py")
# fileList.remove("main.py")
# fileList.remove("__init__.py")
# print fileList

fileList = ['sketchManager.py', 'v2d.py', 'itemclass.py', 'pointclass.py', 'lineclass.py', 'circleclass.py',
            'arcclass.py', 'cons.py', 'operations.py', 'patterns.py', 'shapes.py', 'conCAD.py']

concatFiles('D:\Dropbox\src\Python\conCAD',fileList, "compiled.py")
execfile('D:\Dropbox\src\Python\conCAD\compiled.py')

createSketchIfNoneExist()
clearConsole()
clearDoc()

#ln()

pt1 = pt(v(1, 1))
pt2 = pt(v(2, 2))
ln1 = ln(pt1,pt2)

lns = loop(3,distances=3)

App.activeDocument().recompute()