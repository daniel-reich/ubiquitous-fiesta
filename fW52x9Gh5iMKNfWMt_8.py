
def recaman_index(n):
  seq = [0]
  while n not in seq:
    if seq[-1] - len(seq) >= 0 and seq[-1] - len(seq) not in seq:
      seq += [seq[-1] - len(seq)]
    else:
      seq += [seq[-1] + len(seq)]
  return seq.index(n)

