def remove(a,n):
    f=a[:n-1]
    l=a[n:]
    return f+l
b=str(input('enter a string'))
n=int(input('enter index of the character to be removed'))
print('modified string is')
print(remove(b,n))    
