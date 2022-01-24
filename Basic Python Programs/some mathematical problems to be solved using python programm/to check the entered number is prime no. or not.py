n=int(input("Enter any integer"))
c=n
a=n//2
counter=0
for i in range(2,a+1):
    if(n%i==0):
        counter=counter+1
    break
if(counter==0):
    print(c,"is prime number")
else:
     print(c,"is not prime number")
    
