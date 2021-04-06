
def meme_sum(a, b):
  x = str(a) if len(str(a)) >= len(str(b)) else '0'*(len(str(b)) - len(str(a))) + str(a) 
  y = str(b) if len(str(b)) >= len(str(a)) else '0'*(len(str(a)) - len(str(b))) + str(b)
  z = ''.join(str(int(x[i]) + int(y[i])) for i in range(len(x)))
  return int(z)

