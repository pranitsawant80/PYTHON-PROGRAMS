# def game():
#     return 455


# score= game()
# with open('hiscore.txt')as f:
#     hiscore1=f.read()
# if int(hiscore1)<score or hiscore1=="":
#     with open('hiscore.txt''w') as f:
#         f.write(str(score))
def game():
    return 477

score = game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()
    
if hiScoreStr=='':
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr)<score :
    with open("hiscore.txt", "w") as f:
        f.write(str(score))