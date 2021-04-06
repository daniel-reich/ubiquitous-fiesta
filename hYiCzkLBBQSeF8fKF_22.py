
def count(deck):
  count = 0
  for i in deck:
    if type(i) == str or i == 10:
      count -= 1
    elif i > 6:
      pass
    else:
      count += 1
  return count

