import matplotlib.pyplot as plt
from sympy import Symbol
import numpy as np

x = Symbol('x')

f = (x ** 2) + 3 * x + 5

f_prime = f.diff()

x_list = np.arange(-20, 48, 0.5)
y_list = []

for i in x_list:
    y_list.append(f.subs({ x: i }))


plt.axvline(x=-2/3, color='black', linestyle='--', linewidth=0.8)
plt.axvline(x=0, color='black', linewidth=0.8)
plt.axhline(y=0, color='black', linewidth=0.8)
plt.xlim(-50, 45)
plt.ylim(-5, 90)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')

bench_x = -1 # 기준점
move_x = 9 # 이동점

for j in range(0, 25):
    p = (bench_x, f.subs({ x: bench_x }))
    q = (move_x, f.subs({ x: move_x }))

    average_delta_line = (p[1] - q[1]) / (p[0] - q[0]) * (x - p[0]) + p[1]

    plt.plot(x_list, y_list, color='lime')

    ls = plt.plot(
        x_list,
        [
            average_delta_line.subs({ x : i })
            for i in x_list
        ],
        color='red'
    )

    plt.scatter(*p, color='blue', s=25)
    point = plt.scatter(*q, color='blue', s=25)

    plt.pause(0.001)

    plt.gcf().canvas.draw()
    plt.gcf().canvas.flush_events()

    ls.pop(0).remove()
    point.remove()

    move_x -= 0.4

plt.show()

