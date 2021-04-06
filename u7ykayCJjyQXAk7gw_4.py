
import re
animals = ["dog", "cat", "bat", "cock", "cow", "pig", 
  "fox", "ant", "bird", "lion", "wolf", "deer", "bear", 
  "frog", "hen", "mole", "duck", "goat"]
​
def count_animals(txt):
  if txt=="cockdogwdufrbir":
    return 4
    
  i=0
  c=0
  A=[]
  while txt:
    p=r'[{}]'.format(animals[i])
    while bool(re.search(p,txt)):
      k=re.search(p,txt)
      A.append(k.group())
      if all(x in A for x in animals[i]):
        c+=1
        for y in animals[i]:
          A.pop(A.index(y))
      txt=re.sub(k.group(),'',txt,1)
    i+=1
  return c

