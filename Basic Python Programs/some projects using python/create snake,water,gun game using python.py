#snake water,gun game
import random

def gamewin(a,b):
    if a==b:
        return None
    elif a=='s':
         if b=='w':
             return False
         elif b=="g":
             return True
    elif a=='w':
        if b=='g':
            return False
        elif b=='s':
            return True
    elif a=='g':
        if b=='s':
            return False
        elif b=='w':
            return True


print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
rnd=random.randint(1,3)
if rnd==1:
    a='s'
elif rnd==2:
    a='g'
elif rnd==3:
    a='w'

b=input("YOUR TURN:snake(s),water(w),gun(g) ")
p=gamewin(a,b)
print(f"COMP CHOSE {a}")
print(f"YOU CHOSE {b}")

if p==None:
    print("THE GAME IS TIE ")
elif p:
    print("YOU WIN ")
else:
    print("YOU LOOSE ")