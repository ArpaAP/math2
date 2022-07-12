from sympy import Limit, Symbol

x = Symbol('x')

left_limit = Limit(1/x, x, 0, dir="-").doit()
right_limit = Limit(1/x, x, 0, dir="+").doit()

print('실행 결과는 다음과 같습니다:')
print('극한을 구하려는 함수: y =', 1/x)

print('좌극한:', left_limit, '우극한:', right_limit)

if left_limit == right_limit:
    print('극한값:', left_limit)
else:
    print('따라서 극한값이 없습니다.')

