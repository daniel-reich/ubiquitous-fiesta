
def is_slidey(n):
  if n < 9:
    return True
  return all(abs(int(a) - int(b)) == 1 for a, b in zip(str(n), str(n)[1:]))

