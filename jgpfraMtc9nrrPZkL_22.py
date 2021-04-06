
def switch_gravity_on(lst):
  a = 0
  b = 0
  c = 0
  while b < len(lst[0]):
    while a < len(lst):
      if lst[a][b] == "#":
        lst[a][b] = "-"
        c += 1; a += 1
      else:
        a += 1
    a = len(lst)-1
    while c > 0:
      lst[a][b] = "#"
      c -= 1; a -= 1
    b += 1
    a = 0
    c = 0
  return lst

