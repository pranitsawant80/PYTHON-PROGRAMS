from sympy import Symbol,pprint,factor,init_printing,expand
x=Symbol('x')
y=Symbol('y')
e=x**2-y**2
print(factor(e))
p=(x-y)*(x+y)
print(expand(p))
p1=x*x+x+1
print(factor(p1))
