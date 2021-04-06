
def normal_sequence(n):
  sequence = [0, 1, 1, 2, 0, 2, 2, 1]
  if n<9:
    return sequence[n-1]
  else:
    return sequence[(n-1)%8]

