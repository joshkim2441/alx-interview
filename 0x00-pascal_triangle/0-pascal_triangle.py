#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    triangle = []
    if n <= 0:
        return triangle

    triangle = [[1]]  # Initialize with the first row [1]

    for i in range(1, n):
        row = [1]  # First element of each row is 1
        for j in range(len(triangle[i - 1]) - 1):
            # Calculate the middle elements by summing adjacent elements
            row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        row.append(1)  # Last element of each row is 1
        triangle.append(row)

    return triangle
