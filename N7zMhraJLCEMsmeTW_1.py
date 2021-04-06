
def min_swaps(string):
  com1 = "101010101010101010"[:len(string)]
  com2 = "010101010101010101"[:len(string)]
  i1,i2 = 0, 0
  for s,c1,c2 in zip(string,com1,com2):
    if s != c1: i1 += 1
    if s != c2: i2 += 1
  return min([i1,i2])

