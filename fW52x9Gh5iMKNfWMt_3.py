
def recaman_index(n):
  seq = [0]
  while n not in seq:
    x = seq[-1] - len(seq)
    seq.append(x if x > 0 and x not in seq else seq[-1] + len(seq))
  return seq.index(n)

