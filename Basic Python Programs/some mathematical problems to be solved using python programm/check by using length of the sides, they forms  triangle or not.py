a=float(input("Enter non negative value for 1st side"))
b=float(input("Enter non negative value for 2nd side"))
c=float(input("Enter non negative value for 3rd side"))
if(((a+b)==c)or((a+c)==b)or((b+c)==a)):
    print('This is degenerate triangle')
elif(((a+b)>c)and((a+c)>b)and((b+c)>a)):
    print("This is triangle")
else:
    print("This is not triangle")
