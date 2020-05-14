"""
Make a numpy ndarray np.linspace(5,20,24), and reshape into shape of (4,6).

Split and stack to make array of shape (4,4) such that it contain elements of first, second ,fourth and sixth column.
Split and stack to make array of shape (2,2) such that it contain elements of first and fourth row and third and fifth column."""

import numpy as np

temp_array = np.linspace(5,20,24).reshape(4,6)
print(temp_array)
[A1,A2,A3,A4,A5,A6] = (np.hsplit(temp_array,6))
array_1 = np.stack((A1,A2,A4,A6)).reshape(4,4)
print(array_1)

