n1=int(input('enter no. 1: '))
n2=int(input('enter no. 2: '))
n3=int(input('enter no. 3: '))
n4=int(input('enter no. 4: '))
if (n1>n2 and n1>n3 and n1>n4):
    print(n1,'is the greatest no.')
elif(n2>n3 and n2>n4):
    print(n2,'is the greatest no.')
elif(n3>n4):
    print(n3,'is the greatest no.')
else:
    print(n4,'is the greatest no.')


# num1 = int(input("Enter number 1: "))
#num2 = int(input("Enter number 2: "))
#num3 = int(input("Enter number 3: "))
#num4 = int(input("Enter number 4: "))
#
#if(num1>num4):
#    f1 = num1
#else:
#    f1 = num4
#
#if(num2>num3):
#    f2 = num2
#else:
#    f2 = num3
#
#if(f1>f2):
#    print(str(f1) + " is greatest")
#else:
#   print(str(f2) + " is greatest")