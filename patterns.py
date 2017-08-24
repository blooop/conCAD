from libfunc.mathfuncs import *
from sketchManager import *
from v2d import *
from constraints import *
from pointclass import *
from lineclass import *
from circleclass import *

def pattern(obj,vector,instances):
    output = []

    baseConstruction = ln(dis =vecLen(vector))
    construction = [baseConstruction]
    # ln1 = ln(dis=2)
    # ln1.start.conPoint(origin)
    # ln1.conAng(horAxis, 0.3)
    # for obj in objList:
    vlen = vecLen(vector)
    if isinstance(obj,circle):
        obj.conPoint(baseConstruction.start)
        print v2ad(vector)
        baseConstruction.conAng(horAxis,v2ad(vector))

        for i in range(instances-1):
        #
            tmpln = ln(construction[-1].end,construction=True )
            construction[-1].conAng(tmpln,0)
            output.append(circle(tmpln.start))
            tmpln.conEq(baseConstruction)
            construction.append(tmpln)

        # output[-1]


def symmetric(items,axis):
    return 1