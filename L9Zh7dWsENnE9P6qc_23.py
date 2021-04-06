
def josephus(num):
  return int(bin(num)[3:]+"1", 2) if num > 1 else 1

