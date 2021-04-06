
def is_triangle(*s):
  s = sorted(i for i in s)
  return sum(s[:2]) > s[2]

