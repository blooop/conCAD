from conCAD import *

createSketchIfNoneExist()
clearConsole()
clearDoc()

#ln()

pt1 = pt(v(1, 1))
pt2 = pt(v(2, 2))
ln1 = ln(pt1,pt2)



App.activeDocument().recompute()