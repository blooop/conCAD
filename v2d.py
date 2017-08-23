execfile('D:\Dropbox\src\FreeCAD\conCAD\libfunc\mathfuncs\mathfunc')

#from libfunc.mathfuncs import *
import random
import sketchManager


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