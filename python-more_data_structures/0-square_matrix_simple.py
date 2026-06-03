#!/usr/bin/python3

# square all the values from a matrix

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        new_row = []

        for number in row:
            new_row.append(number ** 2)
        new_matrix.append(new_row)

    return new_matrix
