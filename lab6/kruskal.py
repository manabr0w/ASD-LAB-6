import graph
import vertex
import matrix_utils
import undirected_graph
import turtle
from constants import SEED, NUM_VERTICES, K
import keyboard

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, weight, start_vertex, end_vertex):
        new_edge = vertex.Edge(weight, start_vertex, end_vertex)
        if not self.head or self.head.weight <= new_edge.weight:
            new_edge.next = self.head
            self.head = new_edge
        else:
            current = self.head
            while current.next and current.next.weight > new_edge.weight:
                current = current.next
            new_edge.next = current.next
            current.next = new_edge

    def sort_edges_insertion(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = None  # Початково відсортований список пустий
        current = self.head

        while current:
            next_edge = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_edge

        self.head = sorted_list

    def sorted_insert(self, sorted_head, new_edge):
        if sorted_head is None or sorted_head.weight >= new_edge.weight:
            new_edge.next = sorted_head
            sorted_head = new_edge
        else:
            current = sorted_head
            while current.next and current.next.weight < new_edge.weight:
                current = current.next
            new_edge.next = current.next
            current.next = new_edge
        return sorted_head

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


class Graph:
    def __init__(self, vertices):
        self.edges = LinkedList()
        self.vertices = vertices
        self.matrix = undirected_graph.get_undirected_matrix(matrix_utils.create_directed_matrix(SEED, NUM_VERTICES, K))

    def add_edge(self, weight, start_vertex, end_vertex):
        self.edges.insert(weight, start_vertex, end_vertex)

    def kruskal(self):
        self.edges.sort_edges_insertion()
        uf = UnionFind(self.vertices)
        mst = []
        mst_weight = 0
        current = self.edges.head
        while current:
            u, v = current.start_vertex, current.end_vertex
            if uf.find(u) != uf.find(v):
                mst.append((u, v, current.weight))
                mst_weight += current.weight
                uf.union(u, v)
                turtle.color('red')
                graph.draw_edge(u,v,self.matrix,False,0)
                keyboard.wait('Space')
            current = current.next
        return mst, mst_weight
