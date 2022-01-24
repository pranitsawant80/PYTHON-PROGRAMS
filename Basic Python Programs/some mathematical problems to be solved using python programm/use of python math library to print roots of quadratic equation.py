import math
print("for quadratic eq. of the type ax^2+bx+c=0")
a=float(input("Enter value for a"))
b=float(input("Enter value for b"))
c=float(input("Enter value for c"))
p=(b**2+4*a*c)
if(p>0):
    d=math.sqrt(p)
    x1=(-b+d)/(2*a)
    x2=(-b-d)/(2*a)
    print("roots of quadratic equation are x1= ",x1,"  ,x2= ",x2)
else:
    print("roots of quadratic equation are imaginary")
