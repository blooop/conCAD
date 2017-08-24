from sketchManager import *
from constraints import *
from v2d import *

import pointclass
import circleclass
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

