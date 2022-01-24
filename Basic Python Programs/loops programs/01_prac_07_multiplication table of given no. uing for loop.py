n=int(input('enter the no. for which you want to print the multiplication table\n'))
for i in range(1,11):
    #print(str(n) +" X "+str(i)+ " = " +str(i*n)) OR
    print(f"{n}X{i}={n*i}") #by using f string to reduce typing 