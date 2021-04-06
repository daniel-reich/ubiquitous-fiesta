
def number_split(n):
  list = []
  if n == 0:
    list.extend((0,0))
    return list
  elif n % 2 != 0:
    y = int((n / 2) + .5)
    x = n - y
    list.extend((x, y))
    return list
  else:
    z = n / 2
    list.extend((z,z))
    return list

