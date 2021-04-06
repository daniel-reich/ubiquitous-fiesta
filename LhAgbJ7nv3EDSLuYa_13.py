
def golomb(n):
  seq, i = [1,2,2], 3
  while len(seq)<n:
    seq += [i]*seq[i-1]
    i += 1
  return seq[:n]

