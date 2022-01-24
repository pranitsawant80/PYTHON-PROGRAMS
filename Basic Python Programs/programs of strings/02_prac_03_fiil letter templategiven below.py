letter='''Dear n, 
  you are selected!   
Date: dat '''
name=input("enter your name\n")
date=input("enter your date\n")
letter=letter.replace("n",name)
letter=letter.replace("dat",date)
print(letter)
