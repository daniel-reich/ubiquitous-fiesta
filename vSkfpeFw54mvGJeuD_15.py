
def lychrel(n):
  lych = False
  m = n
  for i in range(500):
    if m != int(str(m)[::-1]):
      m += int(str(m)[::-1])
    else:
      return i
      break
  return True

