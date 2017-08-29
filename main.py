from conCAD import *

#print "releaded"
createSketchIfNoneExist()
clearConsole()
clearDoc()

pt1 = pt(v(1, 1))
pt2 = pt(v(2, 2))
ln1 = ln()

sk().addConstraint(Sketcher.Constraint('Coincident', pt1.id, 1, ln1.end.id, 1))
sk().addConstraint(Sketcher.Constraint('Coincident', pt2.id, 1, ln1.start.id, 1))

#lineStartToPoint(ln1,pt1)
#lns = loop(3,distances=3)

print App.ActiveDocument.Sketch.Geometry

print App.ActiveDocument.Sketch.Constraints


App.activeDocument().recompute()