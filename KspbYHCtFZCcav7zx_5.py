
def bill_split(spicy, cost):
  y, fr = 0, 0
  for f, c in zip(spicy, cost):
    if f == 'S':
      y += c
    else:
      y += c/2
      fr += c/2
  return [y, fr]

