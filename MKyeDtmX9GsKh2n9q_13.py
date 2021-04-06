
import random
def gen_deck():
  l = []
  for i in 'dchs':
    x = [i for i in range(2,15)]
    random.shuffle(x)
    for j in x:
      l.append((j,i))
  return l

