l=['pranit',20,'sawant',45,'abc',123456,'pravin']
p=['hii','whatsapp']
d=[2,6,7,9,5,4,8,1,10]
e='hyphen'
l.append('200')
print(l)

l.extend(p)
print(l)

p.insert(1,'facebook')
print(p)

print(l.count(20))
print(l.index(123456))

d.sort()
print(d)

l.reverse()
print(l)

l.pop(4)
print(l)

l.remove('abc')
print(l)

print(max(d))
print(min(d))
print(list(e))
print(sorted(d))
