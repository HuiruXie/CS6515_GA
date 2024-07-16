import networkx as nx
import random
import unittest
from mst import kruskal, unionFind
from GA_ProjectUtils import Graph


SEED = 1234
random.seed(SEED)


def random_graph(n_upper = 100):
    n = random.randint(10, n_upper + 1)
    m = random.randint(n - 1, n * (n - 1) // 2)
    graph_nx = nx.gnm_random_graph(n, m, seed=SEED)
    edge_data = []
    for (u, v, w) in graph_nx.edges(data=True):
        weight = random.randint(1, 101)
        w["weight"] = weight
        edge_data.append((weight, u, v))

    return graph_nx, Graph(n, edge_data)


class UnionFindTests(unittest.TestCase):
    def test_path_compression(self):
        n = 10
        uf = unionFind(n)
        for i in range(1, n):
            uf.pi[i] = i - 1
            uf.rank[i] = n - i

        uf.rank[0] = n
        uf.find(n - 1)
        self.assertTrue(all(uf.pi[i] == 0 for i in range(n)))

    def test_path_compression_book(self):
        # tests taken from page 136

        uf = unionFind(11)
        uf.pi[1] = 0  # B
        uf.pi[2] = 0  # C
        uf.pi[3] = 2  # D
        uf.pi[4] = 0  # E
        uf.pi[5] = 4  # F
        uf.pi[6] = 4  # G
        uf.pi[7] = 4  # H
        uf.pi[8] = 5  # I
        uf.pi[9] = 5  # J
        uf.pi[10] = 6 # K

        uf.rank[0] = 4
        uf.rank[2] = 2
        uf.rank[4] = 3
        uf.rank[5] = 2
        uf.rank[6] = 2

        self.assertEqual(0, uf.find(8))

        # pointers to A = 0
        self.assertEqual(6, len([i for i in uf.pi if i == 0]))
        for i in [0, 1, 2, 4, 5, 8]:
            self.assertEqual(0, uf.pi[i])

        # pointers to C, E, F
        self.assertEqual(1, len([i for i in uf.pi if i == 2]))
        self.assertEqual(2, len([i for i in uf.pi if i == 4]))
        self.assertEqual(1, len([i for i in uf.pi if i == 5]))

        self.assertEqual(0, uf.find(10))

        # pointers to A = 0
        self.assertEqual(8, len([i for i in uf.pi if i == 0]))
        for i in [0, 1, 2, 4, 5, 6, 10, 8]:
            self.assertEqual(0, uf.pi[i])


class KruskalTests(unittest.TestCase):
    def test_mst(self):
        for _ in range(100):
            graph_nx, graph = random_graph()
            mst, _ = kruskal(graph)
            mst_weight_actual = sum(e[0] for e in mst)

            mst_nx = nx.minimum_spanning_edges(graph_nx, algorithm="kruskal", data=False)
            mst_weight_expected = sum(graph.edgeWts[(u, v)] for u, v in mst_nx)

            self.assertEqual(mst_weight_actual, mst_weight_expected)


if __name__ == '__main__':
    unittest.main()