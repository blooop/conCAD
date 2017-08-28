"""base class for all objects"""
class item:
    globalCounter=0

    def __init__(self):
        globalCounter+=1
        self.uniqueID
        self.children = []
        self.parents = []

    def tickChildren(self):
        for child in self.children:
            child.tickChildren()

