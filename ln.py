from sketchManager import *
from constraints import *
from circle import *
from pt import *
import Sketcher

def line(start=None, end=None, construction=False, name=None):
    if start is None:
        start = randVec()
    if end is None:
        end = randVec()
    id = sk().addGeometry(Part.Line(start, end), construction)
    if name is not None:
        lines[name] = id
    return last()

