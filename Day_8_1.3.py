"""Plot a function of log2 and straight line $y = 0.5x - 1$ using matplotlib and find out approximate value at which they intersect.
 Make sure you have legend in the figure naming the curve."""

import matplotlib.pyplot as plt
import numpy as np

in_array = [1, 1.2, 1.4, 1.6, 1.8, 2]
out_array = np.log2(in_array)

print("out_array : ", out_array)

# plt.plot(in_array, in_array, color='blue', marker="*")

# red for numpy.log2()
plt.plot(out_array, in_array, color='red', marker="o",label="log2(x)")
plt.title("numpy.log2()")
plt.xlabel("out_array")
plt.ylabel("in_array")


""" y = 0.5x - 1"""

x = np.linspace(1,5,6)
y = 0.5*x - 1
plt.plot(x,y,color = 'blue',label="y=0.5x+1")
plt.title("Graph for Line")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()