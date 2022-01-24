x=float(input("Enter X-coordinate"))
y=float(input("Enter y-coordinate"))
if((x!=0)and(y!=0)):
    if((x>0)and(y>0)):
        print("point lies in 1st quadrant")
    elif((x>0)and(y<0)):
        print("point lies in 4rth quadrant")
    elif((x<0)and(y>0)):
        print("point lies in 2nd quadrant")
    elif((x<0)and(y<0)):
        print("point lies in 3rd quadrant")
else:
    print("ERROR")

        
