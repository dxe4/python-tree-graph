import unittest
from simple_graph import Graph, Node

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
        graph = Graph()
        nodes = self.make_nodes()

    def make_nodes(self):
        _chunks = chunks(5, names)
        node_list = lambda _list: [Node(j) for j in _list]
        return [node_list(i) for i in _chunks]

    def test_board_init(self):
        pass


if __name__ == '__main__':
    unittest.main()