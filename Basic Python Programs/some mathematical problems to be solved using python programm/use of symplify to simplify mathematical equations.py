from sympy import sympify
a=str(input('Enter Expression'))
c=2*a
print(c)
try:
    a1=sympify(c)
    except Exception:
        print('String is not valid')
    else:
        print(a1)
        
