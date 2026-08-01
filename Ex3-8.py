import numpy as np
a = 1
c = 3
b = 3000.001
x1 = ((-2 * c) / (b + (b**2 - 4 * a * c)**(1/2)))
x2 = (-2 * c) / (b - (b**2 - 4 * a * c)**(1/2))
print((-0.001 - np.float16(x1))/(-0.001) * 100)
#print(-3000 - np.float32(x2))