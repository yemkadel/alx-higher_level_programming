#!/usr/bin/python3

""" This is the 2 matrix module """


def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        for d_list in matrix:
            if not isinstance(d_list, list):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            for d_num in d_list:
                if (type(d_num) not in [int, float]):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        """
            get the size of each list in the matrix
            then change it to a set, if the lenght of the
            set is more than one, then the list are not of thesame size
        """
        size = len(set([len(d_list) for d_list in matrix]))
        if size > 1:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for d_list in matrix:
        new_d_list = []
        for num in d_list:
            new_d_list.append(round((num / div), 2))
        new_matrix.append(new_d_list)
    return new_matrix
