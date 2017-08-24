# This example is meant to be used from within the CadQuery module of FreeCAD.
# From within FreeCAD, you can make changes to this script and then click
# CadQuery > Execute Script, or you can press F2.
# There are more examples in the Examples directory included with this module.
# Ex026_Lego_Brick.py is highly recommended as a great example of what CadQuery
# can do.

# import sys
# sys.path.append('D:\Dropbox\src\FreeCAD\conCAD')
# execfile('D:\Dropbox\src\FreeCAD\conCAD\FreeCADfuncs.py')

# import conCAD as cc

import cadquery
from Helpers import show

# The dimensions of the box. These can be modified rather than changing the
# object's code directly.
length = 2.0
height = 1.0
thickness = 1.0

# print 1

# App.ActiveDocument=App.getDocument("Unnamed")
# Gui.ActiveDocument=Gui.getDocument("Unnamed")

# def MX12():
# 	lns = loop(4,distances =[16,50,7,50],angles = [-90,90,90],closed=False)
# 	lns[0].start.conPoint(origin)
# 	lns[0].conAng(vertAxis,0)

# 	c1 = circle(1)
# 	c1.conDis(horAxis,21)

# 	ln1 = ln(dis=2)
# 	ln1.start.conPoint(origin)

# #	horAxis.conAng(ln1,45)
# 	ln1.conAng(horAxis, 45)


# 	pattern(c1,v(1,1),3)
# 	#c1.conEdgeDis(lns[-1],2)
# 	#c1.conPoint(lns[-1].end)

# MX12()


# Create a 3D box based on the dimension variables above
result = cadquery.Workplane("XY").box(length, height, thickness)

# Render the solid
show(result)
