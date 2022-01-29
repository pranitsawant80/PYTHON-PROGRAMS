from sympy import Symbol,solve,pprint
x=Symbol('x')
a=Symbol('a')
b=Symbol('b')
c=Symbol('c')
e=x**2+5*x+4
e1=x**2+x+1
e2=x**2*a-b*x+c
print(e)
print(solve(e,dict=True))
print(e1)
pprint(solve(e1,dict=True))
print(e2)
pprint(solve(e2,x,dict=True))


