
def recaman_index(n):
  seq = [0]
  i = 0
  while n not in seq:
    last = seq[-1]
    length = len(seq)
    lml = last - length
    lpl = last + length
    if lml > 0 and lml not in seq:
      seq += [lml]
    else:
      seq += [lpl]
    i += 1
  return seq.index(n)

