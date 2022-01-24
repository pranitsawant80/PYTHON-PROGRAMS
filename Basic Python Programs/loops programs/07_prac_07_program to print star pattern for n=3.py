



# n=int(input('enter a natural no.'))
# for i in range(1,n+1):
#    print(" "*(n-i)+"* "*i)


n=int(input('enter a natural no.'))
for i in range(n): 
    print("  " * (n-i-1), end="")
    print(" *" * (2*i+1), end="")
    print(" " * (n-i-1))




# print("Full Pyramid Pattern of Stars (*): ")
# for i in range(5):
#     for s in range(-6, -i):
#         print(" ", end="")
#     for j in range(i+1):
#         print("* ", end="")
#     print()

'''The ‘end’ is an argument included in the ‘print’ function in Python.
The default value for it is a newline ‘\n’ character.
The ‘end’ specifies the character or string that the print statement should end with.

Below is another example to use where the end value is a space.
for i in range(1,10):
print(i)
it would print no. 1 to 10 horizontally instead of vertically'''
    


