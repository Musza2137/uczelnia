import math
import matplotlib.pyplot as plt

x = []
y = []

for angle in range(0, 361):
    x.append(angle)
    y.append(math.sin(math.radians(angle)))

plt.plot(x, y)
plt.show()
