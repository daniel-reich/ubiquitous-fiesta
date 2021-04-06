
def swap_two(txt):
  a = list(txt)
  for i in range(0, len(a) - len(a) % 4, 4):
    a[i], a[i+1], a[i+2], a[i+3] = a[i+2], a[i+3], a[i], a[i+1]
  return "".join(a)

