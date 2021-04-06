
def normal_sequence(n):
  seq = [0,1]
  for i in range(n-1):
    if len(seq)<8:
      seq.append((seq[-1]+seq[-2])%3)
    else:
      return seq[(n%8)-1]
  return seq

