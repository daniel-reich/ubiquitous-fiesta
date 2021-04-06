
def equal(a, b, c):
  uniq= set([a,b,c])
  if len(uniq)==3:
    return 0
  else:
    return (4 - len(uniq))

