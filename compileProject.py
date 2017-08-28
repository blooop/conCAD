from libfunc.util.IO import *

# fileList = glob.glob("*.py")
# fileList.remove("main.py")
# fileList.remove("__init__.py")
# print fileList

fileList = ['sketchManager.py','v2d.py','itemclass.py','pointclass.py','lineclass.py', 'circleclass.py','arcclass.py','cons.py', 'operations.py', 'patterns.py', 'shapes.py','conCAD.py' ]

folder = 'D:\Dropbox\src\Python\conCAD\'

for i in fileList:
    i = os.path.join(folder,i)

print fileList

concatFiles(fileList,"compiled.py")

execfile('D:\Dropbox\src\Python\conCAD\mcompiled.py')