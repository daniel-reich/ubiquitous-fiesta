
def collect(s, n):
  return sorted([s[i * n : (i + 1) * n] for i in range(len(s) // n)])

