x=int(input("Enter non negative value for x"))
n=int(input("Enter non negative value for n"))
s=0
for i in range(1,n+1,1):
    s=s+(1/(x**i))
print("sum of the serise (1/1+x/2+1/x^2+...1/x^n) is",s)

