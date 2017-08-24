from libfunc.mathfuncs import *
from sketchManager import *
from v2d import *
from constraints import *
from pointclass import *
from lineclass import *
from circleclass import *
import patterns


def filletTri(sideLen):
    line(v(0, 1), v(2, 3))
    conDis(100)
    conHor()
    line(v(2, 3), v(5, 6))
    conEq()
    conCoince()
    line(v(5, 6), v(8, 9))
    conEq()
    conCoince()
    conCoince(0, last(), 1, 2)

    fillets = []
    fillet(10.0, 0, 1)
    fillets.append(last())
    conRad(sideLen / 5.0)
    fillet(10.0, 0, 2)
    fillets.append(last())
    # App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Radius',App.ActiveDocument.Sketch.GeometryCount-1,10))
    fillet(10.0, 1, 2)
    fillets.append(last())
    for i in range(len(fillets) - 1):
        sk().addConstraint(Sketcher.Constraint('Equal', fillets[i], fillets[i + 1]))
    conCoince(-1, 5, 1, 3)
    conDis(sideLen, 0)


def antenna():
    spoke = ln(dis=2)
    rim = ln(dis=1)

    spoke.start.conPoint(origin)
    spoke.end.conPoint(rim.midpoint())
    spoke.perp(rim)

    ln1 = rim.start.lineTo(dis=1.5)
    ln2 = rim.end.lineTo(dis=1.5)
    ln1.end.conPoint(ln2.end)


def trapezoid(parralelDis, leftLen, rightLen, isosolese=True):
    [top, right, bottom, left] = loop(4)
    conPara(top, bottom)
    #	conDis(leftLen,left)
    #	conDis(rightLen,right)
    if isosolese:
        ln1 = line()
        conCoince(ln1, bottom, 2, 1)
        ln2 = line()
        conCoince(ln2, bottom, 2, 2)
        conCoince(ln1, ln2, 1, 1)
        md = midPoint(top)
        #		conEq(ln1,ln2)
        #		conCoince(ln1,md,1)
        #		conPara(ln1,right)
        #		conPara(ln2,left)
        conEq(left, right)

    return [top, right, bottom, left]


# trapezoid(5,1,2)

def trapOld():
    linkLen = 5
    leftRad = 1
    rightRad = leftRad * 2
    [top, right, bottom, left] = loop(4)
    print top
    conSymAxis(top, 2, bottom, 1, -1)
    # conSymAxis(top,1,bottom,2,-1)
    conDis(leftRad, left)
    conDis(rightRad, right)
    conDisAxis(linkLen, right, left, True)
