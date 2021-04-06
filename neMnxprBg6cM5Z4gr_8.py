
def arithmetic_progression(start, diff, n):
  seq = [start]
  for i in range(n-1):
    seq.append(seq[i]+diff)
  return ', '.join(str(i) for i in seq)

