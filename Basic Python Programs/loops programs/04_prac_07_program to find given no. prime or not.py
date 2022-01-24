n=int(input('enter no. to check prime or not '))
p=int(n/2)
prime=True
for i in range(2,p):
     if(n%i==0):
          prime=False
          break
if prime:
     print(n,' is prime ')
else:
     print(n,' is not prime ')