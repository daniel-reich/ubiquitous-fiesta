
def perrin(n):
  seq = [3,0,2]
  if n == 1 or n == 2 or n == 0:
    return seq[n]
  for x in range(n-2):
    seq.append(seq[x]+seq[x+1])
  return seq[-1]

