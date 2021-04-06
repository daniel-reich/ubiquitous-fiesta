
def add_odd_to_n(n):
  return ((n + 1) * (((n - 1)//4) + 0.5)) if (n + 1) % 4 != 0 else (n + 1) * ((n + 1) // 4)

