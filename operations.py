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
    return objectsf


def fillet(rad, obj1=None, obj2=None):
    if obj1 is None:
        obj1 = last() - 1
    if obj2 is None:
        obj2 = last()
    sk().fillet(obj1, obj2, rad)
