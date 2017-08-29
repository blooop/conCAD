from conCAD import *
import collections
import nodeclass
#print "releaded"
createSketchIfNoneExist()
clearConsole()
clearDoc()

pt1 = pt(v(1, 1))
pt2 = pt(v(2, 2))
ln1 = ln(pt1,pt2)

lns = loop(3)

tree = nodeclass.TraversalResult()

#print tree.allNodes
# pt1.traverse(tree)

lns[0].traverse(tree)

#print "tree:", tree

print "tree"
for i in tree.allNodes:
    print type(i), "id: ", i.id

print "lines"
print tree.lines

print "points"
print tree.points

# sk().addConstraint(Sketcher.Constraint('Coincident', pt1.id, 1, ln1.end.id, 1))
# sk().addConstraint(Sketcher.Constraint('Coincident', pt2.id, 1, ln1.start.id, 1))

#lineStartToPoint(ln1,pt1)
#lns = loop(3,distances=3)

if False:
    print App.ActiveDocument.Sketch.Geometry
    print App.ActiveDocument.Sketch.Constraints


App.activeDocument().recompute()