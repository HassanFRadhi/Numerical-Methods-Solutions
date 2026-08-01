import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(4,4.5,100)
y = np.sin(10 * x) + np.cos(3 * x)
plt.figure()
plt.plot(x,y)
plt.grid(True)
plt.ylim([-0.15, 0.15])
plt.xlim([4, 4.5])
plt.show()