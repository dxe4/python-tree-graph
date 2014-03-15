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

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return str(self.data)


class TreeGraph(object):
    def __init__(self):
        self.nodes = [[]]
        self.edges = defaultdict(list)

    def add_node(self, node, depth, parent=None):
        if not depth + 1 <= len(self.nodes):
            self.nodes.append([])
        self.nodes[depth].append(node)
        if parent:
            self.add_edge(parent, node)

    def add_edge(self, node_a, node_b):
        self.edges[node_a].append(node_b)

    def __eq__(self, other):
        if other is None or not isinstance(other, TreeGraph):
            return False
        return self.edges == other.edges and self.nodes == other.nodes

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def visit(self, node, _dict):
        children = self.edges[node]
        _dict[node] = {} if children else None
        for i in children:
            self.visit(i, _dict[node])
        return _dict

    def to_dict(self):
        return [self.visit(i, {}) for i in self.nodes[0]]
