from v2d import *

import cons
import nodeclass
import circleclass
import lineclass

#reload(circleclass)
#reload(lineclass)

class pt(nodeclass.Node):
    def __init__(self, pos=None, defineOrigin=False):
        super(pt, self).__init__()
        self.pntType = 1
        if not defineOrigin:
            self.pos = pos or v()
            self.id = sk().addGeometry(Part.Point(self.pos))


    def vertex(pos):
        output = pt()
        output.id = sk().addGeometry(Part.Point(self.pos))

    @classmethod
    def lineStart(self,line1):
        output = pt(defineOrigin = True)
        output.id = line1.id
        output.pntType = 1
        return output

    @classmethod
    def lineEnd(self, line1):
        output = pt(defineOrigin=True)
        output.id = line1.id
        output.pntType = 2
        return output

    @classmethod
    def arcCenter(arc1):
        output = pt(defineOrigin=True)
        output.id = arc1.id
        output.pntType = 3
        return output

    @classmethod
    def origin():
        output = pt(defineOrigin=True)
        output.pos = v(0, 0)
        output.id = -1
        return output

    def subTraverse(self,result):
        result.points.append(self)

    def conPoint(self, pnt):
        sk().addConstraint(Sketcher.Constraint('Coincident', self.id, self.pntType, pnt.id, pnt.pntType))

    # def lineTo(self, otherPoint=None, dis=None):
    #     tmp = lineclass.ln(self, otherPoint, dis)
    #     return tmp

    def moveTo(self,pos):
        print self.id,self.pntType,pos
        App.ActiveDocument.Sketch.movePoint(0, 1, App.Vector(0.576531, 0.717636, 0), 0)
        #sk().movePoint(self.id,self.pntType,pos,0)

    def lineTo(self, otherPoint=None, dis=None):
        tmp = lineclass.ln(start = self, end = otherPoint, dis= dis)
        return tmp

    def conVert(self, point):
        lineclass.ln(self, point, construction=True).conVert()

    def conDis(self, point, dis):
        conId = sk().addConstraint(Sketcher.Constraint('Distance', self.id, 1, point.id, 1, dis))
        sk().setDatum(conId, App.Units.Quantity(str(dis) + ' mm'))


class pt1(nodeclass.Node):
    def __init__(self, pos=None, defineOrigin=False):
        nodeclass.Node.__init__(self)
        if not defineOrigin:
            self.pos = pos or v()
            self.id = sk().addGeometry(Part.Point(self.pos))

    def origin(self):
        self.pos = v(0, 0)
        self.id = -1

    def subTraverse(self,result):
        result.points.append(self)

    def conPoint(self, pnt):
        otherid = 1
        if isinstance(pnt, circleclass.circle):
            otherid = 3
        sk().addConstraint(Sketcher.Constraint('Coincident', self.id, 1, pnt.id, otherid))

    def lineTo(self, otherPoint=None, dis=None):
        tmp = lineclass.ln(self, otherPoint, dis)
        return tmp

    def conVert(self, point):
        lineclass.ln(self, point, construction=True).conVert()

    def conDis(self, point, dis):
        conId = sk().addConstraint(Sketcher.Constraint('Distance', self.id, 1, point.id, 1, dis))
        sk().setDatum(conId, App.Units.Quantity(str(dis) + ' mm'))


def defineOriginPt():
    origin = pt(defineOrigin=True)
    origin.id = -1
    return origin


origin = defineOriginPt()
