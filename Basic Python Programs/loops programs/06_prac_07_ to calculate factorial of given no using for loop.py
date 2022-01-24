n=int(input('The no. for which factorial of the no is to be calculated '))
fact=1
for i in range(1,n+1):
    fact=fact*i
#print('factorial of given no.is '+str(fact) )
print(f'factorial of given no. {n} is {fact}')  #By using f string