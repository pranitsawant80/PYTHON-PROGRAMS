import random
randomNo=random.randint(1,100)
print(randomNo)

guesses=0

Userguess=int(input("Guess the no. \n"))


while Userguess!=randomNo:

    if (Userguess<randomNo):
        Userguess=int(input("Your guessed it WRONG ,Enter higher No.\n "))

    else: 
        Userguess=int(input("Your guessed it WRONG,Enter Lower  No.\n "))
     
    if  Userguess==randomNo:
        print('Your guessed it RIGHT, the no. was ', randomNo,'\n')
    guesses=guesses+1
   


print(f"NO. of guesses you took is, {guesses+1}\n")


with open ('score1.txt','r') as f:
    highscore=int(f.read())

if(guesses<highscore):
    print("You have just cracked the highest score ")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))