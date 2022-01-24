with open('this.txt') as f:
    content1 =f.read()
with open('copy.txt')as p :
    content2=p.read()
if content1==content2:
    print('The given file have similar content')
else:

    print('The given file have dissimilar content')