
def soroban(frame):
  fives = reversed([int(elem == '|') for elem in frame[0]])
  ones = reversed([col.index('|') for col in zip(*frame[3:])])
  total = 0
  for pv, (n, f) in enumerate(zip(ones, fives)):
    total += (10 ** pv) * (5*f + n)
  return total

