from conCAD import *

print "releaded"
createSketchIfNoneExist()
clearConsole()
clearDoc()

pt1 = pt(v(1, 1))
pt2 = pt(v(2, 2))
ln1 = ln(pt1,pt2)

#lns = loop(3,distances=3)

App.activeDocument().recompute()