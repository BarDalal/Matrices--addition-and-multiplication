# -*- coding: utf-8 -*-
"""
Name: Bar Dalal
Class: Ya4

The program adds the common parts of two matrices. 
The sum's size is as the common part's size.
"""

import numpy as np

def MinAddition(a, b):
    """
    The function gets two matrices.
    The function returns the sum of the common parts of the matrices (minimum size). 
    """
    if (a.shape[0] >= b.shape[0]):
        x= b.shape[0]
    else:
        x= a.shape[0]
        # x is the minimum number of rows from the two matrices
    if (a.shape[1] >= b.shape[1]):
        y= b.shape[1]
    else:
        y= a.shape[1]
        # y is the minimum number of columns from the two matrices
    c= np.zeros([x,y], dtype = int) # the sum of the common parts of the matrices
    for row in range(x):
        for column in range (y):
            c[row, column]= a[row, column] + b[row, column]
    return c


def main():
    arr = np.array([[1, 2, 3, 7], [4, 5, 6, 90], [7, 8, 9, 6]])
    arr2= np.array([[10, 20, 50],[30, 40, 20], [1, 2, 3], [6, 8, 0]])
    result= MinAddition(arr, arr2)
    print (result)
    


if __name__ == "__main__":
    main()
