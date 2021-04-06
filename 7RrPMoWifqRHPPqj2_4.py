
def safecracker(s, increments):
  i, j, k = increments
  return [(s - i) % 100, (s - i + j) % 100, (s - i + j - k) % 100]

