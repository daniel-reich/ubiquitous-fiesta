
def chocolates_parcel(n_small, n_big, order):
​
  if (2 * n_small) + (5 * n_big) < order:
    return -1
  if (2 * n_small) + (5 * n_big) == order:
    return n_small
  else:
    possibilites = []
    for i in range(1, n_big + 1):
      if (order - (5 * i)) % 2 == 0:
        possibilites.append(i * 5)
      for i in possibilites:
        if i > order:
          possibilites.remove(i)
    if len(possibilites) > 0:
      return (order - max(possibilites)) / 2
    else:
      for x in range(1, n_small + 1):
        if x * 2 == order:
          return x
  return -1

