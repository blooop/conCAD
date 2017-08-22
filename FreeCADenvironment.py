import sys
sys.path.append('C:\Program Files\FreeCAD 0.16')

import FreeCAD

App = FreeCAD
import FreeCADGui
Gui = FreeCADGui

import Sketcher

import Draft, Part
from FreeCAD import Gui

import random
from PySide import QtGui
import math
import collections

lines = dict()
loops = []

PI = math.pi
PI2 = math.pi * 2.0
PIB2 = math.pi / 2.0

def a2v(angle):
    return v(math.cos(angle), math.sin(angle))

def lerp(value, inputLow, inputHigh, outputLow, outputHigh):
    return outputLow + ((value - inputLow) / (inputHigh - inputLow)) * (outputHigh - outputLow)

def clearConsole():
    mw = Gui.getMainWindow()
    c = mw.findChild(QtGui.QPlainTextEdit, "Python console")
    c.clear()
    r = mw.findChild(QtGui.QTextEdit, "Report view")
    r.clear()




def delGeometry(index):
    App.ActiveDocument.Sketch.delGeometry(index)


def clearAll():
    doc = App.ActiveDocument
    for obj in doc.Objects:
        doc.removeObject(obj.Label)

def randVec(instances=1):
    if instances > 1:
        output = []
        for i in range(instances):
            output.append(v(random.random(), random.random()))
        return output
    return v(random.random(), random.random())

def v(x=0, y=0):
    return App.Vector(x, y, 0)



def last():
    return App.ActiveDocument.Sketch.GeometryCount - 1

def sk():
    return App.ActiveDocument.Sketch