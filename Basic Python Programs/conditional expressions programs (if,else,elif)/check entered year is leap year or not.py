Y=int(input("enter the year"))
if(Y%400==0):
    print(Y," is leap year")
elif(Y%100==0):
    print(Y,"is not leap year")
elif(Y%4==0):
    print(Y," is leap year")
else:
    print(Y,"and is not leap year")
