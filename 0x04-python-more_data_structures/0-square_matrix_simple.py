#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = list(map(lambda x : x**x, matrix))
    return res
