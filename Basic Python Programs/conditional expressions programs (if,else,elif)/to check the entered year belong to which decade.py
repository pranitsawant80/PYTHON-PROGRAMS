y=int(input("Enter Year"))
if((y>=1920)and(y<=1970)):
    if((y>=1920)and(y<=1929)):
        print("20's decade")
    elif((y>=1930)and(y<=1939)):
        print("30's decade")
    elif((y>=1940)and(y<=1949)):
        print("40's decade")
    elif((y>=1950)and(y<=1959)):
        print("50's decade")
    elif((y>=1960)and(y<=1969)):
        print("60's decade")
    elif(y==1970):
        print("70's decade")
else:
    print("Out of range")
    
