import matplotlib.pyplot as plt
import numpy as np
import math
m = 68.1
c = 12.5
g = 9.81
dt = 0.1
tgoal = 10
x = 0
x1 = []
t1 = []
v1 = []
for i in np.arange(0,10.1,dt):
    xi = x
    t = i
    x = xi + dt * g * m /c * (1 - math.exp(-c * t / m))
    x1.append(x)
    t1.append(t)
    v1.append(g * m /c * (1 - math.exp(-c * t / m)))
#print(x)
v = g * m /c * (1 - math.exp(-c * t / m))
#print(v)
plt.figure()
plt.plot(t1, x1)
plt.plot(t1,v1)
plt.show()