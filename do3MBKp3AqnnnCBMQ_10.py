
import random
def numbers():
  l = ""
  while len(l) < 5:
    x = random.randint(1,5)
    if str(x) not in l:
      l += str(x)
  return int(l)

