
import random
def numbers():
  l = [1,2,3,4,5]
  myans = ''
  while len(myans) < 5:
    x = random.randint(0,len(l)-1)
    myans += str(l[x])
    del l[x]
  return int(myans)

