"""base class for all objects"""
class baseitem(object):

    globalCounter=0

    def __init__(self):
        #globalCounter+=1
        self.uniqueID = self.globalCounter
        self.children = []
        self.parents = []
        self.nodes = []

    def traverse(self,result):
        print "allNodes", self.nodes
        for node in self.nodes:
            print "curNode: ", node
            if node not in result:
                result[node] =node.id
                node.traverse(result)


