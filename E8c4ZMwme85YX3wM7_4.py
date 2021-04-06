
def recaman(n):
  seq = []
  x = 0
  dup = []
  for i in range(n):
    x = x - i
    if x>=0 and x not in seq:
      pass
    else:
      x = x + 2*i
      if x in seq and x not in dup:
        dup.append(x)
    seq.append(x)
  return "---> Recaman's sequence: {}\n---> Duplicates for n = {}: {}".format(seq, n, dup)

