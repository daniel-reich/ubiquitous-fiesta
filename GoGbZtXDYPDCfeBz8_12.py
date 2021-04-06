
def magic(txt):
  a = txt.split()
  return any([int(a[0]) * int(a[1]) == int(a[2][i:]) for i in range(1,4)])

