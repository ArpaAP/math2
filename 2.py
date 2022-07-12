from sympy import Symbol

x = Symbol('x')

f = (x ** 2) + 3 * x + 5

print(f.subs({ x: 5 }))

