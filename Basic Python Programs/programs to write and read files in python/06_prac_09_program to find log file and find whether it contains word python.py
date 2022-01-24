
with open('log.txt') as c:
    f=c.read()
    if 'python' in f.lower():
        print("the file contain word, python ")
    else:
        print("the file dose not contain word, python ")