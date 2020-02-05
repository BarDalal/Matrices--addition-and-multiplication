# -*- coding: utf-8 -*-
"""
Name: Bar Dalal
Class: Ya4

The program does matrix multiplication without using matmul
"""

import numpy as np


def MatMul(a,b):
    """
    The function gets two matrices and returns their multiplication matrix
    Note: The number of columns in matrix a equals to the number of rows in matrix b
    """
    c= np.zeros([a.shape[0], b.shape[1]], dtype = int) # the product of the matrices which are parameters  
    x= a.shape[0] # number of rows in matrix a
    y= b.shape[1] # number of columns in matrix b
    for row in range(x):
        for column in range (y):
            c[row, column]= CalcElement(a[row], b[:,column]) 
    return c


def CalcElement(a,b):
    """
    The function gets a row from one martix and a column from the other matrix
    The function calculates and returns the element in the multiplication matrix which is placed in this intersection (row, column)
    """
    res= 0 # the number in the specific element of the proudct matrix
    for element in range (len(a)):
        res = res + a[element]*b[element]
    return res


def main():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    #print (arr, "\n")
    arr2= np.array([[1, 2, 3], [2, 4, 6], [1, 3, 5]])
    #print (arr2, "\n")
    print ("From matmul: \n" , np.matmul(arr, arr2))
    
    res= MatMul(arr, arr2)    
    print (" \n Mine:", res)
 
  
if __name__ == "__main__":
    main()
