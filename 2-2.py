import matplotlib.pyplot as plt
from sympy import Symbol
import numpy as np

x = Symbol('x')

f = (x ** 0.5)

x_list = np.arange(-1, 11, 0.1)
y_list = []

for i in x_list:
    y_list.append(f.subs({ x: i }))

plt.axvline(x=-2/3, color='black', linestyle='--', linewidth=0.8)
plt.axvline(x=0, color='black', linewidth=0.8)
plt.axhline(y=0, color='black', linewidth=0.8)
plt.xlim(-25, 20)
plt.ylim(-5, 40)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x_list, y_list)

plt.show()

