
def is_orthogonal(first, second):
  a = len(first)
  c = 0
  for x in range(a):
    c = c + (int(first[x]) * int(second[x]))
  if c == 0:
    return True
  return False

