"""Make a ndarray by using np.arange(120), reshape it into shape of (2,3,4,5) and do the following operation on this new ndarray:

Access the value 91 using indexing
obtain a range of value 35-39 from this ndarray
Make another 1D array from this having values 0 and all multiples of 5
obtain mean values on axis-3 elements."""

import numpy as np
temp_array = np.arange(120).reshape(2,3,4,5)

res = temp_array[1,1,2,1]
print(res)
result = np.where(np.logical_and(temp_array>= 35, temp_array<= 39))
print("result" , result)
temp_array_1d = np.arange(0,120,5)
print("1D_array " , temp_array_1d)

m = temp_array.mean(axis = 3)
print("mean ",m)

