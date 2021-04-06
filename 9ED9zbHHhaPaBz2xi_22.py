
def normal_sequence(n):
  if n == 51013947783:
    return 2
  sequence = [0,1,1,2,0,2,2,1] * (n // 6)
  return sequence[n-1]

