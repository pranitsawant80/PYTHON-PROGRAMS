f=True

with open('log.txt') as c:
    i=1  
    while f:
         f=c.readline()
      
         if 'python' in f.lower():
            print(f)
            print(f"Yes python is present on line no.{i}")
      
         i=i+1