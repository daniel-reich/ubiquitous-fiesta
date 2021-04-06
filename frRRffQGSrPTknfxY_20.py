
def digit_count(n):
  s = str(n)
  return int(''.join(str(s.count(d)) for d in s))

