
def is_slidey(n):
  return all(abs(int(a)-int(b)) == 1 for a, b in zip(str(n), str(n)[1:]))

