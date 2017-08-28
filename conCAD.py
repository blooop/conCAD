from libfunc.mathfuncs import *
from sketchManager import *
from v2d import *
from cons import *
from pointclass import *
from lineclass import *
from circleclass import *
from patterns import *
from operations import *
from shapes import *
from itemclass import *
#import reimport

def main():
    createSketchIfNoneExist()
    clearConsole()
    clearDoc()
    test()
    App.activeDocument().recompute()

if __name__ == "__main__":
    print "asdf"
    ln()
    #ln()
    #ln()
    #lns = loop(6)
