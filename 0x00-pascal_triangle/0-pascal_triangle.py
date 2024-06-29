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
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row [1]

    for i in range(1, n):
        row = [1]  # First element of each row is 1
        for j in range(1, i):
            # Calculate the middle elements by summing adjacent elements
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Last element of each row is 1
        triangle.append(row)

    return triangle
