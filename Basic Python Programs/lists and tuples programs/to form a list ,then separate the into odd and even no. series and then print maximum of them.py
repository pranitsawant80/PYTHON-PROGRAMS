n=int(input('enter number of terms you want in serise'))
l=[]
for i in range(0,n):
    a=int(input('enter integer element'))
    l.append(a)
even=[]
odd=[]
for i in l:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
d=max(even)
c=max(odd)
print("The largest even number in the list is ",d)
print("The largest odd number in the list is ",c)
  
