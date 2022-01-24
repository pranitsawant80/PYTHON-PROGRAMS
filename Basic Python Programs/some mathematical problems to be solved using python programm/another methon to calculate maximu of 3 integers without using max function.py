x=int(input("Enter non negative 1st integer"))
y=int(input("Enter non negative 2nd integer"))
z=int(input("Enter non negative 3rd integer"))
if(x>y):
    if(x>z):
        m=x
    else:
        m=z
elif(y>z):
    m=y
else:
    m=z
print("maximum integer among 3 integers is ",m)
