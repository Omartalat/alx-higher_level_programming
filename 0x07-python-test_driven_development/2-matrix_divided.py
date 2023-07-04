#!/usr/bin/puthon3
def matrix_divided(matrix, div):
    nmatrix = []
    row_size = len(matrix[0])
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for row in matrix:
        if len(row) != row_size:
            raise TypeError('Each row of the matrix must have the same size')
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        nrow = []
        for element in row:
            nrow.append(round(element / div, 2))
        nmatrix.append(nrow)
    return nmatrix
