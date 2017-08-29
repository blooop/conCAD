from lineclass import *


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

def fillet3(point,rad):
    trav = point.traverse(maxDepth=1)
    print trav.lines[0].id
    print trav.lines[1].id
    print trav.points
    return sk().fillet(trav.lines[0].id, trav.lines[1].id, rad)
    #point.traverse(maxDepth=1).lines