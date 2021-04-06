
def arithmetic_progression(start, diff, n):
  tn = start + (n - 1) * diff
  if diff == 0:
    return ", ".join([str(i) for i in str(start) * n])
  return ", ".join([str(i) for i in range(start, tn+diff, diff)])

