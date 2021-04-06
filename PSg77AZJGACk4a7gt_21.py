
def meme_sum(a, b):
  a = str(a)
  b = str(b)
  la = len(a)
  lb = len(b)
  a = a if la > lb else '0' * (lb - la) + a
  b = b if lb > la else '0' * (la - lb) + b
  return int(''.join(str(int(i) + int(j)) for i, j in zip(a, b)))

