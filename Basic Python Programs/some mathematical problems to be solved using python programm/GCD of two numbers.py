a=int(input("Enter non negative 1st no."))
b=int(input("Enter non negative 2nd no."))
c=a
d=b
while(a!=b):
     if(a>b):
         a=a-b
     else:
         b=b-a
print("GCD of ",c,"and",d,"is",b)
        
            
