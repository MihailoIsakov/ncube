import numpy as np


def adjacency_matrix(dim=3):
    size = 2**dim
    matrix = np.zeros((size, size))
    indices = range(size)

    for i in indices:
        matrix[i, size-i-1] = 1
        for bit in range(dim):
            bit_select = 1 << bit
            matrix[i, i ^ bit_select] = 1

    return matrix


def connected(dim, max_steps):
    mat = np.matrix(adjacency_matrix(dim))

    return mat**(max_steps-1) + mat**(max_steps)

