from sympy import Symbol,pprint,init_printing
def ps(n,x_v):
    init_printing(order='rev-lex')
    x=Symbol('x')
    s=1
    for i in range(1,n):
        s=s+(i+1)*(x**i)
    pprint(s)
    s_v=s.subs({x:x_v})
    print('value of the series at{0}= {1}'.format(x_v,s_v))
if(__name__=='__main__'):
    a=int(input('enter no. of term you want in series'))
    x_v=int(input('enter no. of term you want in series'))
    ps(a,x_v)
