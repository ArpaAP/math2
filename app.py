from sympy import Add, Symbol, solve

x = Symbol('x')

f: Add = Add(0)
f_prime = f.diff()
f_prime_prime = f_prime.diff()

rsts = solve(f_prime)

i = [(i, f.subs({x: i})) for i in rsts if f_prime_prime.subs({x: i}) > 0]
a = [(i, f.subs({x: i})) for i in rsts if f_prime_prime.subs({x: i}) < 0]

print('구하려는 함수: y =', f)
print('결괏값은 다음과 같습니다:')
print('극대:', ', '.join(map(lambda x: f'x={x[0]} 에서 {x[1]}', a)))
print('극소:', ', '.join(map(lambda x: f'x={x[0]} 에서 {x[1]}', i)))


