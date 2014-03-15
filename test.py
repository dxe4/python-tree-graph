from simple_graph import TreeGraph, Node
import unittest

names = ["Sophia", "Emma", "Olivia", "Isabella", "Ava", "Lily", "Zoe", "Chloe", "Mia",
         "Madison", "Emily", "Ella", "Madelyn", "Abigail", "Aubrey", "Addison",
         "Avery", "Layla", "Hailey", "Amelia", "Hannah", "Charlotte", "Kaitlyn", "Harper",
         "Kaylee", "Sophie", "Mackenzie", "Peyton", "Riley", "Grace", "Brooklyn",
         "Sarah", "Aaliyah", "Anna", "Arianna", "Ellie", "Natalie", "Isabelle",
         "Lillian", "Evelyn", "Elizabeth", "Lyla", "Lucy", "Claire", "Makayla", "Kylie",
         "Audrey", "Maya", "Leah", "Gabriella", "Annabelle", "Savannah", "Nora", "Reagan",
         "Scarlett", "Samantha", "Alyssa", "Allison", "Elena", "Stella", "Alexis",
         "Victoria", "Aria", "Molly", "Maria", "Bailey", "Sydney", "Bella", "Julia",
         "Mila", "Taylor", "Kayla", "Eva", "Jasmine", "Gianna", "Alexandra", "Eliana",
         "Kennedy", "Brianna", "Ruby", "Lauren", "Alice", "Violet", "Kendall", "Eleanor",
         "Morgan", "Caroline", "Piper", "Brooke",
         "Elise", "Alexa", "Sienna",
         "Reese", "Clara", "Paige", "Kate", "Nevaeh", "Sadie", "Quinn", "Isla",
]


def chunks(size, _list):
    list_size = len(_list)
    assert list_size % size == 0
    new_list_size = list_size / size
    temp = [(int((i - 1) * new_list_size), int(new_list_size * i))
            for i in range(1, size + 1)]
    return [_list[i[0]:i[1]] for i in temp]


class TestAdding(unittest.TestCase):
    def setUp(self):
        self._list = names
        self.chunk_size = 5
        self.graph = TreeGraph()
        node_chunks = chunks(self.chunk_size, self._list)
        last = None
        for depth, node_list in enumerate(node_chunks):
            for count, node in enumerate(node_list):
                parent = last[count] if last else Node
                self.graph.add_node(node, depth, parent=parent)
            last = node_list

    def test_init(self):
        assert sum([len(i) for i in self.graph.nodes]) == len(self._list)
        assert len([len(i) for i in self.graph.nodes]) == self.chunk_size
        assert self.graph.to_dict()["Sophia"] == {
            'Hannah': {'Elizabeth': {'Alexis': {'Lauren': None}}}}


class TestAdding2(unittest.TestCase):
    def setUp(self):
        self.graph = TreeGraph()
        self.nodes = names

    def test_add(self):
        root = self.nodes.pop(0)
        self.graph.add_node(root, 0)
        depth = 1
        parent = root
        for count, i in enumerate(self.nodes):
            self.graph.add_node(i, depth, parent=parent)
            if (count + 1) % 10 == 0:
                depth += 1
                parent = i

        _dict = self.graph.to_dict()
        _keys = _dict["Sophia"]["Emily"]["Hannah"]["Brooklyn"].keys()
        assert len(_keys) == 10


class TestReadable(unittest.TestCase):
    def setUp(self):
        self.graph = TreeGraph()
        self.graph.add_node("Bob", 0)
        self.graph.add_node("Alice", 0)

        self.graph.add_node("Tom", 1, parents=["Bob", "Alice"])
        self.graph.add_node("Alex", 1, parents=["Bob", "Alice"])

        for i in ("Sophia", "Emma", "Olivia", "Isabella"):
            self.graph.add_node(i, 2, parent="Tom")

        for i in ("Lillian", "Evelyn", "Elizabeth"):
            self.graph.add_node(i, 2, parent="Alex")

    def test_add(self):
        _dict = self.graph.to_dict()
        assert "Bob" in _dict.keys()
        assert "Alice" in _dict.keys()
        assert _dict["Bob"].keys() == _dict["Alice"].keys()


if __name__ == '__main__':
    unittest.main()