from sympy import Symbol,pprint,init_printing
x=Symbol('x')
y=Symbol('y')
print(x+x+x+2)
s=x*x*x+y*y*y
print(s)
pprint(s)
init_printing(order='rev-lex')
w=x*x+2*x+5
pprint(w)
print(x.name)
p=x*x+2*x*x+2*x+55
pprint(p)


