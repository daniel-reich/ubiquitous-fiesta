
from random import randint
def numbers():
  lst = []
  while len(lst)<5:
    temp = randint(1,5)
    if temp not in lst:
      lst.append(temp)
  return int(''.join([str(i) for i in lst]))

