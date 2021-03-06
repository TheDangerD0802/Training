import numpy as np
import matplotlib.pyplot as plt
velocity = int(input("enter velocity  "))
angle = int(input("enter angle  "))
velocity_x = velocity*np.cos(np.pi/180*angle)
velocity_y = velocity*np.sin(np.pi/180*angle)
if(angle==90):
    velocity_x= 0
g = 9.8
time = int((2*velocity_y)//g)
distance_x = []
distance_y = []
for t in range(0,(time+1)*100):
    s_x = velocity_x * (t/100)
    s_y = velocity_y * (t/100) - (1 / 2) * (g) * (t/100) * (t/100)
    if(s_y>0):
        distance_y.append(s_y)
        distance_x.append(s_x)
distance_x = np.array(distance_x)
distance_y = np.array(distance_y)
plt.xlabel("distance_x")
plt.ylabel("distance_y")
plt.plot(distance_x, distance_y)
plt.show()
