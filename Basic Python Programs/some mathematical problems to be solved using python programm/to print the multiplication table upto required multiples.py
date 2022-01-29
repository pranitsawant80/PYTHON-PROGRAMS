def multitable(a,b):
    for i in range(1,b+1):
         print('{0}*{1}={2}'.format(a,i,a*i))
if(__name__=='__main__'):
    m=int(input('enter a number for which we have calculate multiplication table '))
    n=int(input('number up to which we have to calculate multiplicatio table  '))
    multitable(m,n)

