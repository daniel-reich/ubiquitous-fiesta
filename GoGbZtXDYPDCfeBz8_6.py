
def magic(txt):
  a = txt.split()
  b = int(a[0]) * int(a[1])
  c = len(str(b))
  if c == 1:
    return b == int(a[-1][-1])
  elif c == 2:
    return b == int(a[-1][-2:])

