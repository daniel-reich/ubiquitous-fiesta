
def guess_sequence(n):
  increase = 90
  current = 0
  for x in range(n):
    current += increase
    increase += 60
  return current

