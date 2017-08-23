from libfunc.mathfuncs import *
from sketchManager import *
import random

def randVec(instances=1):
    if instances > 1:
        output = []
        for i in range(instances):
            output.append(v(random.random(), random.random()))
        return output
    return v(random.random(), random.random())

def v(x=0, y=0):
    return App.Vector(x, y, 0)

def a2v(angle):
    return v(math.cos(angle), math.sin(angle)+10)

def a2vd(angle):
    angle *= deg2rad
    return v(math.cos(angle), math.sin(angle))