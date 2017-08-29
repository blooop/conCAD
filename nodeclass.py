"""base class for all objects"""
# import pointclass
# import lineclass

class TraversalResult(object):
    def __init__(self):
        self.allNodes = dict()
        self.points = []
        self.lines = []
        self.a = 1


class Node(object):

    globalCounter=0

    def __init__(self):
        #globalCounter+=1
        self.uniqueID = self.globalCounter
        self.children = []
        self.parents = []
        self.nodes = []

    def traverse(self,result):
        for node in self.nodes:
            if node not in result.allNodes:
                result.allNodes[node] = node.id
                # if isinstance(pointclass.pt):
                #     result.points.append(node)
                # if isinstance(lineclass.ln):
                #     result.points.append(node)

                node.traverse(result)


