
def golomb(n):
  seq = [1]
  while len(seq) < n:
    seq.append(seq[-1]+(seq.count(seq[-1])==seq[seq[-1]-1]))
  return seq

