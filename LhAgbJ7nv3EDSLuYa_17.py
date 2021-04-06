
def golomb(n):
  seq = [1]
  idx  = 1
  while len(seq) < n:
      if idx < len(seq):
        seq.extend([idx + 1] * seq[idx])
      else:
        seq.extend([idx + 1] * (idx + 1))
  return seq[:n]

