
def closing_in_sum(n):
  n = str(n)
  if len(n) < 2: return int(n or "0")
  return int(n[0] + n[-1]) + closing_in_sum(n[1:-1])

