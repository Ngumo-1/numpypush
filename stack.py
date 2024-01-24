import numpy as np
from numpy import random

arr1=np.random.rand(3,3)
arr2=np.random.rand(3,3)


def row_stacking(arr1, arr2):
    return np.hstack((arr1, arr2))

def column_stacking(arr1, arr2):
    return np.vstack((arr1, arr2))

xarr=column_stacking(arr1, arr2)
print(xarr)
print('\n')
# varr=np.vstack((arr1,arr2))
# print(varr)