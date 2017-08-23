from v2d import *
#from ln import ln
#from circle import circle
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



