
def invert(s, acc='', i=0):
  if i == len(s): return acc
  return invert(s, s[i].swapcase() + acc, i+1)

