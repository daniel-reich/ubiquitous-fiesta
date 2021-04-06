
import random
def numbers():
  lst = [1, 2, 3, 4, 5]
  random.shuffle(lst)
  return int("".join(map(str, lst)))

