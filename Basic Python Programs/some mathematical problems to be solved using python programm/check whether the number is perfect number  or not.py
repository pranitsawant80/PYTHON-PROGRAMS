n=int(input("Enter positive intger"))
p=n
s=0
d=(n//2)
for i in range(1,d+1):
      if(n%i==0):
         s=s+i
     
if(s==p):
     print("The given no.is perfect number")
else:
     print("The given no. is not perfect number")
