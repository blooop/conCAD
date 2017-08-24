from v2d import *

import circleclass
import lineclass
from constraints import *

class pt:
    def __init__(self, pos=None,defineOrigin = False):
        if not defineOrigin:
            self.pos = pos or v()
            self.id = sk().addGeometry(Part.Point(self.pos))

    def origin(self):
        self.pos = v(0, 0)
        self.id = -1

    def conPoint(self, pnt):
        otherid = 1
        if isinstance(pnt,circle):
            otherid = 3
        sk().addConstraint(Sketcher.Constraint('Coincident', self.id, 1, pnt.id, otherid))

    def lineTo(self, otherPoint=None, dis=None):
        tmp = ln(self, otherPoint, dis)
        return tmp

    def conVert(self,point):
        ln(self,point,construction=True).conVert()

    def conDis(self,point,dis):
        conId = sk().addConstraint(Sketcher.Constraint('Distance',  self.id,1,point.id,1, dis))
        sk().setDatum(conId,App.Units.Quantity(str(dis) +' mm'))

class circle:
    def __init__(self,rad = None,pos=None,construction=False):
        self.rad = rad
        self.pos = pos or pt()
        # sk().addGeometry(Part.Circle(pos,App.Vector(0, 0, 1), rad),construction=construction)
        self.id = sk().addGeometry(Part.Circle(),construction)
        self.center = pt()
        if self.rad is not None:
            conRad(self.rad,self.id)
        # if pos is not None:

    def conPoint(self,pnt):
        sk().addConstraint(Sketcher.Constraint('Coincident',self.id,3,pnt.id,1))

    def conDis(self,obj,dis):
        if isinstance(obj, pt):
            sk().addConstraint(Sketcher.Constraint('Distance', obj.id, dis))
        elif isinstance(obj, ln):
            sk().addConstraint(Sketcher.Constraint('Distance',self.id,3,obj.id, dis))

    def tangent(self,obj):
        print "s"
        if isinstance(obj,ln):
            sk().addConstraint(Sketcher.Constraint('Tangent', obj.id, self.id))
        else:
            raise Exception("tangent must be a curve")

    def conEdgeDis(self,obj,dis):
        conDis(obj,self.rad+dis)

class ln:
    def __init__(self, start=None, end=None, dis=None, construction=False,defineOrigin = False):
        if not defineOrigin:
            self.start = start or pt()
            self.end = end or pt()
            self.id = sk().addGeometry(Part.Line(), construction)
            self._midpoint = None

            if dis is not None:
                self.conLen(dis)

            sk().addConstraint(Sketcher.Constraint('Coincident', self.start.id, 1, self.id, 1))
            sk().addConstraint(Sketcher.Constraint('Coincident', self.end.id, 1, self.id, 2))

    def midpoint(self):
        if self._midpoint is None:
            self._midpoint = pt()
            sk().addConstraint(Sketcher.Constraint('Symmetric', self.start.id, 1, self.end.id, 1, self._midpoint.id, 1))
        return self._midpoint

    def conLen(self, dis):
        if dis is not None:
            conDis(dis, self.id)
        else:
            print "cannot constrain length to None"

    def perp(self, line1):
        conPerp(self.id, line1.id)

    def conHor(self):
        sk().addConstraint(Sketcher.Constraint('Horizontal', self.id))

    def conVert(self):
        sk().addConstraint(Sketcher.Constraint('Vertical', self.id))

    def conAng(self, line1,angle):

        tmp = sk().addConstraint(Sketcher.Constraint('Angle',self.id,1,line1.id,1,angle))
        sk().setDatum(tmp, App.Units.Quantity(str(angle)+' deg'))

    def conEq(self,line1):
        sk().addConstraint(Sketcher.Constraint('Equal', self.id, line1.id))

