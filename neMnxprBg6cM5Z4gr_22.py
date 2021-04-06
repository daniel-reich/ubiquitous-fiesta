
def arithmetic_progression(s, d, n):
  return ', '.join(map(str, [i * d + s for i in range(n)]))

