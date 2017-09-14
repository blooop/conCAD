import collections

import libfunc.mathfuncs

reload(libfunc.mathfuncs)
from libfunc.mathfuncs import *

import sketchManager

reload(sketchManager)
from sketchManager import *

import v2d

reload(v2d)
from v2d import *

import pointclass

reload(pointclass)
from pointclass import *

import lineclass

reload(lineclass)
from lineclass import *

import circleclass

reload(circleclass)
from circleclass import *

import cons

reload(cons)
from cons import *

import patterns

reload(patterns)
from patterns import *

import operations

reload(operations)
from operations import *

import shapes

reload(shapes)
from shapes import *

import nodeclass

reload(nodeclass)
from nodeclass import *

createSketchIfNoneExist()
clearConsole()
clearDoc()

# append(
# loops.append(polyLine2(points, distances, angles=angles, closeLoop=closed, construction=False))
# return loops[-1]

# pt1 = pt(v(1, 1))
# pt1.moveTo(v(1,2))
# pt2 = pt(v(2, 2))
# ln1 = ln(v(1,1), v(1,2))

# ln1.end.moveTo(v(2,1))
# ln2 = ln1.end.lineTo()

loop(3, [None, 2, 2])

# loop(4,[1,1,2,None])

# loop(5,2)

# fillet_triangle(1)


# ln1.lineTo()
# ln2 = ln()

# ln1.end.conPoint(ln2.end)
# print ln1.end
# ln2 = ln1.end.lineTo(v(2,2))
# ln1.end.lineTo()
#  #pt(v(1,0))
# ln(pt(v(1,0)))
# ln()

# lns =loop2(3)

# exit()

if False:
    # print tree.allNodes
    # pt1.traverse(tree)

    tree = lns[0].traverse()

    t2 = lns[0].start.traverse(maxDepth=1)

    # fillet3(lns[0].start,3)

    print "t2lines ", t2.lines
    # print "tree:", tree

    print "tree"
    for i in tree.allNodes:
        print type(i), "id: ", i.id

    print "lines"
    print tree.lines

    print "points"
    print tree.points

    # sk().addConstraint(Sketcher.Constraint('Coincident', pt1.id, 1, ln1.end.id, 1))
    # sk().addConstraint(Sketcher.Constraint('Coincident', pt2.id, 1, ln1.start.id, 1))

    # lineStartToPoint(ln1,pt1)
    # lns = loop(3,distances=3)

    if False:
        print App.ActiveDocument.Sketch.Geometry
        print App.ActiveDocument.Sketch.Constraints

App.activeDocument().recompute()
