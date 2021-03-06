import Part
import Sketcher

import lineclass
import pointclass
from sketchManager import *


class circle:
    def __init__(self, rad=None, pos=None, construction=False):
        self.rad = rad
        self.pos = pos or pointclass.pt()
        # sk().addGeometry(Part.Circle(pos,App.Vector(0, 0, 1), rad),construction=construction)
        self.id = sk().addGeometry(Part.Circle(), construction)
        self.center = pointclass.pt()
        if self.rad is not None:
            self.conRad(self.rad)
            # if pos is not None:

    def conRad(self, rad):
        sk().addConstraint(Sketcher.Constraint('Radius', self.id, self.rad))

    def conPoint(self, pnt):
        sk().addConstraint(Sketcher.Constraint('Coincident', self.id, 3, pnt.id, 1))

    def conDis(self, obj, dis):
        if isinstance(obj, pointclass.pt):
            sk().addConstraint(Sketcher.Constraint('Distance', obj.id, dis))
        elif isinstance(obj, lineclass.ln):
            sk().addConstraint(Sketcher.Constraint('Distance', self.id, 3, obj.id, dis))

    def tangent(self, obj):
        print "s"
        if isinstance(obj, lineclass.ln):
            sk().addConstraint(Sketcher.Constraint('Tangent', obj.id, self.id))
        else:
            raise Exception("tangent must be a curve")

    def conEdgeDis(self, obj, dis):
        sk().addConstraint(Sketcher.Constraint('Distance', self.id, self.rad + dis))
        # constraints.conDis(obj,self.rad+dis)

        # pt1 = pt()
        # pt2 = pt(v(1,1))
        # sk().addConstraint(Sketcher.Constraint('Coincident',self.id,3,pt1.id, 1))
        # sk().addConstraint(Sketcher.Constraint('PointOnObject',pt2.id,1, self.id))

        # ln1 = ln(pt1,pt2,construction=True)
        # ln1.start.conPoint(self.id)
        # sk().addConstraint(Sketcher.Constraint('Coincident', ln1.id,1, self.id,3))
        # sk().addConstraint(Sketcher.Constraint('PointOnObject', ln1.id,2, self.id))
        # ln1.end.
        # addConstraint(Sketcher.Constraint('PointOnObject', 14, 2, 11))
