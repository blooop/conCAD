from sketchManager import *
from constraints import *
from circle import circle
from pt import *
import Sketcher

def line(start=None, end=None, construction=False, name=None):
    if start is None:
        start = randVec()
    if end is None:
        end = randVec()
    id = sk().addGeometry(Part.Line(start, end), construction)
    if name is not None:
        lines[name] = id
    return last()

class ln:
    def __init__(self, start=None, end=None, dis=None, construction=False,defineOrigin = False):
        if not defineOrigin:
            self.start = start or pt()
            self.end = end or pt()
            self.id = line(construction=construction)
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