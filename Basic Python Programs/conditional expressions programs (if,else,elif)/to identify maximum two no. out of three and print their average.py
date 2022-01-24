a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=max(a,b,c)
if(d==a):
    if(b>c):
        print(a,b,'are the maximum numbers and their average is',(a+b)/2)
    else:
        print(a,c,'are the maximum numbers and their average is',(a+c)/2)
elif(d==b):
    if(a>c):
        print(a,b,'are the maximum numbers and their average is',(a+b)/2)
    else:
        print(c,b,'are the maximum numbers and their average is',(c+b)/2)
elif(d==c):
    if(b>a):
        print(b,c,'are the maximum numbers and their average is',(b+c)/2)
    else:
        print(a,c,'are the maximum numbers and their average is',(a+c)/2)    
