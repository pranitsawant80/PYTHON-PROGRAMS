def factor(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
a=int(input('enter a number whose factors are to be calculate'))
factor(a)
