
def last(a, n):
  num = []
  if n == 0:
    return num
  elif n > len(a):
    return "invalid"
  else:
    return a[-n:]

