
def meme_sum(a, b):
  a,b = str(a) , str(b)
  z = "0" * abs(len(a)-len(b))
  if len(a)> len(b):
    b = list(z+b)
  else:
    a = list(z+a)
    
  return int("".join([str(int(i)+int(j)) for i,j in zip(a, b)]))

