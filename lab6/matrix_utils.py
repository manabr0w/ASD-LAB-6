import random
import math


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


def create_directed_matrix(seed, length, k):
    random.seed(seed)
    matrix = [[random.uniform(0, 2) for _ in range(length)] for _ in range(length)]
    direct_matrix = [[math.floor(matrix[i][j] * k) for j in range(length)] for i in range(length)]
    return direct_matrix

def weight_matrix(matrix):
    B = [[random.uniform(0.0, 2.0) for j in range(12)] for i in range(12)]
    C = [[0 for j in range(12)] for i in range(12)]
    D = [[0 for j in range(12)] for i in range(12)]
    H = [[0 for j in range(12)] for i in range(12)]
    Tr = [[0 for j in range(12)] for i in range(12)]
    W = [[0 for j in range(12)] for i in range(12)]
    for i in range(12):
        for j in range(12):
            C[i][j] = int(round((matrix[i][j] * 100 * B[i][j]), 0))
            if C[i][j] > 0:
                D[i][j] = 1
            if i < j:
                Tr[i][j] = 1
    for i in range(12):
        for j in range(12):
            if D[i][j] != D[j][i]:
                H[i][j] = 1
    for i in range(12):
        for j in range(12):
            W[i][j] = (D[i][j] + H[i][j] * Tr[i][j]) * C[i][j]
            W[j][i] = W[i][j]

    return W





