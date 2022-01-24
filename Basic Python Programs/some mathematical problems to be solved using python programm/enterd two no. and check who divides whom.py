a=int(input('enter first number'))
b=int(input('enter second number'))
if(a>b):
   if(a%b==0):
      print(a,'is','divisible by',b)
   else:
       print(a,'is not','divisible by',b)
elif(b%a==0):
     print(b,'is','divisible by',a)
else:
     print(b,'is not','divisible by',a)
