s=0
c=0
for i in range(10,101,1):
    if(i%2==0):
       s=s+i**2
    else:
       c=c+i**3
print("sum of the squares of even integers between 10 to 100 is",s)


print("sum of the cubes of odd integers between 10 to 100 is",c)

