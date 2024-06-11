import turtle

from constants import SEED, NUM_VERTICES, K
from graph import draw_graph
from matrix_utils import print_matrix, create_directed_matrix, weight_matrix
from kruskal import *


def get_undirected_matrix(direct_matrix):
    size = len(direct_matrix)
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if direct_matrix[i][j]:
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix

def main():
    a = Graph(12)
    directed_matrix = create_directed_matrix(SEED, NUM_VERTICES, K)
    undirected_matrix = get_undirected_matrix(directed_matrix)
    W = weight_matrix(undirected_matrix)
    print('Undirected matrix:')
    print_matrix(undirected_matrix)
    print('\n')
    print_matrix(W)
    print('\n')
    draw_graph(undirected_matrix, False,W)
    for i in range(12):
        for j in range(i):
            if undirected_matrix[i][j] > 0:
                a.add_edge(W[i][j], i, j)
    edges, tW = a.kruskal()
    for edge in edges:
        print(f"Start: {edge[0]+1}, End: {edge[1]+1}, Weight: {edge[2]}")
    print("Total weight:", tW)
    turtle.exitonclick()



if __name__ == '__main__':
    main()
