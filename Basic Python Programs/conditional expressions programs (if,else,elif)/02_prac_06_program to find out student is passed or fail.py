s1=int(input("enter marks of subject 1:\n"))
s2=int(input("enter marks of subject 2:\n"))
s3=int(input("enter marks of subject 3:\n"))
per=(s1+s2+s3)/3
r=s1>33 and s2>33 and s3>33
if(per>40 and r): 
     print('The student is passed ')
else: 
    print('The student is failed ')

 


#sub1 = int(input("Enter first subject marks\n"))
#sub2 = int(input("Enter second subject marks\n"))
#sub3 = int(input("Enter third subject marks\n"))
#
#if(sub1<33 or sub2<33 or sub3<33):
#    print("You are fail because you have less than 33% in one of the subjects")
#elif(sub1+sub2+sub3)/3 < 40:
#    print("You are fail due to total percentage less than 40")
#else:
#    print("Congatulations! You passed the exam")