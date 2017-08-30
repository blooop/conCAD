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




#lns = loop(3)

def polyLine2(pointsList, distances=None, angles=None, closeLoop=False, construction=False):
    lineIndices = []
    lineIndices.append(ln(pointsList[0], pointsList[1], construction=construction))

    for i in range(2, len(pointsList)):
        lineIndices.append(lineIndices[-1].end.lineTo(pointsList[i]))
    if closeLoop:
        lineIndices.append(lineIndices[-1].end.lineTo(lineIndices[0].start))

    if distances is not None:
        distanceDict = dict()

        if not isinstance(distances, collections.Iterable):
            distanceDict[distances] = range(len(lineIndices))
            lineIndices[0].conLen(distances)
            for i in range(1, len(lineIndices)):
                lineIndices[0].conEq(lineIndices[i])
        else:
            for i in range(len(distances)):
                if not distances[i] in distanceDict:
                    distanceDict[distances[i]] = [i]
                else:
                    distanceDict[distances[i]].append(i)

        for key, value in distanceDict.iteritems():
            if len(value) > 1:
                lineIndices[value[0]].conLen(key)
                for i in range(1, len(value)):
                    lineIndices[value[0]].conEq(lineIndices[value[i]])
            else:
                lineIndices[value[0]].conLen(key)

    if angles is not None:
        angles = makeSureIsList(angles, len(pointsList))
        for i in range(len(lineIndices) - 1):
            lineIndices[i].conAng(lineIndices[i + 1], angles[i])

    return lineIndices

def loop2(num, distances=None, angles=None, closed=True, construction=False):
    points = []
    if not closed:
        num += 1
    for i in range(num):
        points.append(a2v(PIB2 + lerp(i, 0.0, num, 0.0, PI2)))
    loops.append(polyLine2(points, distances, angles=angles, closeLoop=closed, construction=False))
    return loops[-1]

pt1 = pt(v(1, 1))
#pt2 = pt(v(2, 2))
ln1 = ln()

#ln1.end.lineTo()
#  #pt(v(1,0))
# ln(pt(v(1,0)))
#ln()

#lns =loop2(3)


#exit()

if False:
    #print tree.allNodes
    # pt1.traverse(tree)

    tree = lns[0].traverse()

    t2 = lns[0].start.traverse(maxDepth=1)

    #fillet3(lns[0].start,3)

    print "t2lines ", t2.lines
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