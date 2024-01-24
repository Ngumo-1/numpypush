import numpy as np
from concatenate import concatenate_arrays
from stack import column_stacking, row_stacking
arr1=np.random.randint(100, size=(3,3))
# arr3=arr1.reshape(-1)
arr2=np.random.randint(100, size=(3,3))
# arr4=arr2.reshape(-1)
# axis=0
#
# xarr=concatenate_arrays(arr1, arr2, axis)
# print(xarr)

xarr=column_stacking(arr1, arr2)
print(xarr)
print('\n')
# varr=np.vstack((arr1,arr2))
# print(varr)