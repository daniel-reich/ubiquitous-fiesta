
def parity_analysis(n):
  return 1 - (n + sum(int(d) for d in str(n))) % 2

