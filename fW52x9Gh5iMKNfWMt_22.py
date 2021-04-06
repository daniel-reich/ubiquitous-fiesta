
def recaman_index(n):
  seq = [0]
  while seq[-1] != n:
    temp = seq[-1] - len(seq)
    if temp > 0:
      if temp not in seq:
        seq.append(temp)
      else:
        temp = seq[-1] + len(seq)
        seq.append(temp)
    else:
      temp = seq[-1] + len(seq)
      seq.append(temp)
  return seq.index(n)

