# c=open('pranit.txt','r')
# f=c.read()
# f=f.replace('donkey','########')
# c.close()
# c=open('pranit.txt','w')
# p=c.write(f) 
# c.close()

with open("pranit.txt") as f:
    content = f.read()

content = content.replace("donkey", "#########")

with open("pranit.txt", "w") as f:
    f.write(content)


    