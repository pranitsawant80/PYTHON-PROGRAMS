#n=int(input('enter a natural no.'))
#for i in range(1,n+1):
#    print(" "*(n-i)+"* "*i)
#for i in range(n-1,0,-1):
#    print(" "*(n-i)+"* "*i)#







print("Inverted Half Pyramid of Stars (*):")
for i in range(5):
    for j in range(i, 5):
        print(" * ", end=" ")
    print()


    """print("Full Pyramid Pattern of Stars (*): ")
for i in range(5):
    for s in range(-6, -i):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()"""