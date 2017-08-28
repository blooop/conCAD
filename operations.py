from libfunc.mathfuncs import *
from sketchManager import *
from v2d import *
from constraints import *
from pointclass import *
from lineclass import *
from circleclass import *
import patterns


def applyProperty(objects, propertyItemOrList, func):
    propertyItemOrList = makeSureIsList(propertyItemOrList, len(objects))
    if propertyItemOrList is not None:
        for i in range(len(objects)):
            objects[i] = func(objects[i], propertyItemOrList[i])
    return objects

def fillet(rad, obj1=None, obj2=None):
    print obj1.id
    print obj2.id
    return sk().fillet(obj1.id, obj2.id, rad)

def fillet2(rad, obj1=None, obj2=None):
    return sk().fillet(obj1, obj2, rad)