words=['mote','kaddu','kutte']
with open("pranit.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#########")

    with open("pranit.txt", "w") as f:
         f.write(content)