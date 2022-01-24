import math
x=float(input("Enter X-coordinate"))
y=float(input("Enter y-coordinate"))
r=float(input("Enter Radius of circle"))
c=math.sqrt(x**2+y**2)
if(c<=r):
    print("A given point ",x,"and",y,"belongs to circle")
else:
    print("A given point ",x,"and",y,"dose not belongs to circle")
    
