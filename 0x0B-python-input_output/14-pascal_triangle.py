#!/usr/bin/python3


def pascal_triangle(n):
    """
    prints n lines of Pascal's Triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    tri = [[1], [1, 1]]
    if n == 2:
        return tri

    i = 2
    while i < n:
        j = 0
        row = [1, 1]
        while j < i - 1:
            sum = tri[i-1][j] + tri[i-1][j+1]
            row.insert(j+1, sum)
            j += 1
        tri.append(row)
        i += 1
    return tri
