
def arithmetic_progression(start, diff, n):
  return ', '.join(str(n * diff + start) for n in range(n))

