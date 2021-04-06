
def is_repeated(s):
  i = (s + s).find(s, 1, -1)
  return False if i == -1 else s.count(s[:i])

