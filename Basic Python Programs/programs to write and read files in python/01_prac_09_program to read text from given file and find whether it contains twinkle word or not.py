# import os
# os.getcwd()
f= open('poems.txt')
p= f.read()
print(p)

if('twinkle' in p):
    print('The word twinkle is in poem')
else:
    print('The word twinkle is not in poem')
f.close()