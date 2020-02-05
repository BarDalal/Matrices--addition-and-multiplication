# -*- coding: utf-8 -*-
"""
Name: Bar Dalal
Class: Ya4

The program adds two matrices thus the not common elements contain zeros 
"""

import numpy as np

def AddMaxPart(a, b):
    """
    The function gets two matrices.
    The function returns the sum of the matrices thus the not common elements contain zeros (maximum size)
    """
    if (a.shape[0] >= b.shape[0]):
        x= a.shape[0] 
        x1= b.shape[0] 
    else:
        x= b.shape[0]
        x1= a.shape[0]
    # x is the maximum number of rows from the two matrices
    # x1 is the minimum number of rows from the two matrices
    if (a.shape[1] >= b.shape[1]):
        y= a.shape[1]
        y1= b.shape[1]
    else:
        y= b.shape[1]
        y1= a.shape[1]
    # y is the maximum number of columns from the two matrices
    # y1 is the minimum number of columns from the two matrices
    c= np.zeros([x,y], dtype = int) # the sum of the matrices thus the not common elements contain zeros
    for row in range(x1):
        for column in range (y1):
            c[row,column]= a[row,column] + b[row, column]
    return c


def main():
    arr = np.array([[1, 2, 3, 7], [4, 5, 6, 90], [7, 8, 9, 6]])
    arr2= np.array([[10, 20, 50],[30, 40, 20], [1, 2, 3], [6, 8, 0]])
    result= AddMaxPart(arr, arr2)
    print (result)
    
    
    
if __name__ == "__main__":
    main()
