
def break_point(num):
  s = str(num)
  l = [int(i) for i in list(s)]
  return any(sum(l[:i]) == sum(l[i:]) for i in range(1, len(l)))

