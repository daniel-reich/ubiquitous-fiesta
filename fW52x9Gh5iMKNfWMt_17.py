
def recaman_index(n):
  seq, x = [0], 0
  while x != n:
    x = seq[-1] - len(seq)
    if x > 0 and x not in seq:
      seq.append(x)
    else:
      x = seq[-1] + len(seq)
      seq.append(x)
  return len(seq) - 1

