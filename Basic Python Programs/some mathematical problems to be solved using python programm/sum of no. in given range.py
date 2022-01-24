x=int(input("Enter non negative 1st integer"))
y=int(input("Enter non negative 2nd integer"))
s=0
for i in range(x,y+1,1):
    s=s+i
print("Sum of numbers in given range is",s)
