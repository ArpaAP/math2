from sympy import Limit, Symbol

x = Symbol('x')

f = (x ** 2) + 3 * x + 5

h = Symbol('h')

fxh = f.subs({ x: x + h })
fx = f.subs({ x: x })

f_prime = Limit((fxh - fx) / h, h, 0).doit()

print(f_prime)

