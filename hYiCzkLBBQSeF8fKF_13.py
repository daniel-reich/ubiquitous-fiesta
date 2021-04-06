
def count(deck):
  a = [2, 3, 4, 5, 6 ]
  b = [7, 8, 9]
  c = [10, 'J', 'Q', 'K', 'A']
  d = 0
  if not deck:
    return 0
  for i in deck:
    if i in a:
      d += 1
    elif i in b:
      d += 0
    else:
      d -= 1
  return d

