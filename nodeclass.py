"""base class for all objects"""


class TraversalResult(object):
    def __init__(self):
        self.allNodes = dict()
        self.points = []
        self.lines = []
        self.constraints = []
        self.a = 1


class Node(object):
    globalCounter = 0

    def __init__(self):
        # globalCounter+=1
        self.uniqueID = self.globalCounter
        #self.children = []
        #self.parents = []
        self.nodes = set()
        self.id = None

    def link(self,other):
        self.nodes.add(other)
        other.nodes.add(self)

    def traverse(self, result=None, maxDepth=5000, depth=0):
        if result == None:
            result = TraversalResult()
        #print depth
        if depth <= maxDepth:
            for node in self.nodes:
                if node not in result.allNodes:
                    result.allNodes[node] = node.id
                    node.subTraverse(result)
                    node.traverse(result, maxDepth=maxDepth, depth=depth + 1)
        return result
