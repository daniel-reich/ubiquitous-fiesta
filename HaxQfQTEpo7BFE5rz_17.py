
def alternate_pos_neg(lst):
  if 0 in lst:
    return False
  l = []
  evens = [lst[i] for i in range(0, len(lst), 2)]
  odds = [lst[i] for i in range(1, len(lst), 2)]
  if lst[0] > 0:
    for i in evens:
      if i < 0:
        l.append(False)
    for i in odds:
      if i > 0:
        l.append(False)
  if lst[0] < 0:
    for i in evens:
      if i > 0:
        l.append(False)
    for i in odds:
      if i < 0:
        l.append(False)
  return all(l)

