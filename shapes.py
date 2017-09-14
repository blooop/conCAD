from circleclass import *
from lineclass import *
from pointclass import *


def fillet_triangle(sideLen):
    lns = loop(3, sideLen)
    # for i in range(len(lns)):
    #     lns[i].start.fillet()


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


def circleTest():
    lns = loop(3)
    lns[0].start.conPoint(origin)
    lns[0].conEq(lns[1])
    lns[1].conEq(lns[2])
    c = circle(2)

    c.tangent(lns[0])
    c.tangent(lns[1])
    c.tangent(lns[2])


#	c.conDis(lns[0],2)
#	c.conDis(lns[1],2)
#	c.conDis(lns[2],2)

def sawTooth():
    lns = loop(8, closed=False)
    lns[0].start.conVert(lns[2].end)
    lns[4].start.conVert(lns[6].end)
    lns[2].start.conVert(lns[4].end)
    for i in range(len(lns)):
        if i % 2 == 0:
            lns[i].conHor()
        else:
            lns[i].conVert()


# lns[0].start

def MX12():
    lns = loop(4, distances=[16, 50, 7, 50], angles=[-90, 90, 90], closed=False)
    lns[0].start.conPoint(origin)
    lns[0].conAng(vertAxis, 0)

    c1 = circle(1)
    c1.conDis(horAxis, 21)
    c1.conDis(lns[0], 5)

    # horAxis.conAng(ln1,45)
    # ln1.conAng(horAxis, 45)

    pattern(c1, v(8, 0), instances=5)


#	lns = list(map((lambda x: x.
# lns[2].start.conPoint(origin)

def test():
    pt1 = pt(v(1, 1))
    pt2 = pt(v(2, 2))
    ln1 = ln(pt1, pt2)
