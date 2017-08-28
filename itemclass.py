"""base class for all objects"""
class baseitem(object):

    globalCounter=0

    def __init__(self):
        #globalCounter+=1
        self.uniqueID = self.globalCounter
        self.children = []
        self.parents = []
        self.nodes = []

    def tickChildren(self):
        for child in self.children:
            child.tickChildren()

