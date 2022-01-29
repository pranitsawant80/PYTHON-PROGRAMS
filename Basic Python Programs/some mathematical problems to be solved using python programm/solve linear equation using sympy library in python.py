from sympy import Symbol,solve
x=Symbol('x')
y=Symbol('y')
e1=2*x+3*y-6
e2=3*x+2*y-12
print(e1)
print(e2)
print(solve((e1,e2),x,y,dict=True))