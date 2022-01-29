from sympy import Symbol,Subs,pprint,simplify
x=Symbol('x')
y=Symbol('y')
e=x*(x+y)-(x+y)*y
print(e)
print(simplify(e))

