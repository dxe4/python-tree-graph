class Node(object):
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        if other is None or not hasattr(other, "data"):
            return False
        if self.data == other.data:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)



class Graph(object):
    def __init__(self):
        self.nodes = {}
        self.edges = {}

