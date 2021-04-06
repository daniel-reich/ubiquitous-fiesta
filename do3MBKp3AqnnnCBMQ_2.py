
def numbers():
  from random import randint
  num = ""
  while len(num) < 5:
    temp = str(randint(1, 5))
    num += temp if temp not in num else ''
  return int(num)

