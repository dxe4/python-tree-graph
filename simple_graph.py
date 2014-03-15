from collections import defaultdict

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
        self.nodes = list()
        self.edges = defaultdict(list)

    def add_node(self, node, parent=None):
        self.nodes.append(node)
        if parent:
            self.add_edge(parent, node)

    def add_edge(self, node_a, node_b):
        self.edges[node_a].append(node_b)

    def __eq__(self, other):
        if other is None or not isinstance(other, Graph):
            return False
        return self.edges == other.edges and self.nodes == other.nodes

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)
