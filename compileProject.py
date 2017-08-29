from libfunc.util.IO import *

# fileList = glob.glob("*.py")
# fileList.remove("main.py")
# fileList.remove("__init__.py")
# print fileList

fileList = ['sketchManager.py', 'v2d.py', 'nodeclass.py', 'pointclass.py', 'lineclass.py', 'circleclass.py',
            'arcclass.py', 'cons.py', 'operations.py', 'patterns.py', 'shapes.py', 'conCAD.py']

concatFiles('D:\Dropbox\src\Python\conCAD',fileList, "compiled.py")