
def is_undulating(n):
  s, m = str(n), str(n % 100)
  return n > 99 and s.count(m) == len(s) // 2

