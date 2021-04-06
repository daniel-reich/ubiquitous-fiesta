
def numbers():
  import random
  ls = []
  while True:
    x = random.randint(1, 5)
    if not str(x) in ls:
      ls.append(str(x))
    if len(ls)==5:
      return int("".join(ls))

