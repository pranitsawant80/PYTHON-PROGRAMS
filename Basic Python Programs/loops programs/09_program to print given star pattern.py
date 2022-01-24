n=int(input('enter a natural no.'))


# print("* "*i)
# print("*  ",end='')
# print(" ",end='')
# print("*")
# print("* "*i)

print("* "*n)
c=n-2
for i in range(c): 
    print("* ", end="")
    print("  " * c, end="")
    print("*")
print("* "*n)
    