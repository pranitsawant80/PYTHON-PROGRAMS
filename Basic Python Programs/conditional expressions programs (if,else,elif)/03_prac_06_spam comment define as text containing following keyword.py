p=input('enter a comment\n')
a=p.lower()  # if user enters lower and upper case characters then this makes all string in lower case and then accurate result
c="make a lot of money"
d="buy now"
e="subscribe this"
f="click this"
#if(c in a ):
#    print("the comment is spam")
#elif(d in a):
#    print("the comment is spam")
#elif(e in a):
#    print("the comment is spam")
#elif(f in a):
#    print("the comment is spam")
#else:
#    print("The message is text message")



if(c in a or d in a or f in a or e in a ):
    print("the comment is spam")
else:
    print("The message is text message")


#text = input("Enter the text\n")
#
#if("make a lot of money" in text):
#    spam = True
#elif("buy now" in text):
#    spam = True
#elif("click this" in text):
#    spam = True
#elif("subscribe this" in text):
#    spam = True
#else:
#    spam = False
#
#if(spam):
#    print("This text is spam")
#else:
#    print("This text is not spam")