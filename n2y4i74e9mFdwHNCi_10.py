
def get_items_at(lst, par, res = []):
  if par == 'even':
    for i in range(len(lst)):
      if i % 2:
        res = res + [lst[::-1][i]]
      if i == len(lst) - 1:
        return res[::-1]
  else:
    for i in range(len(lst)):
      if not i % 2:
        res = res + [lst[::-1][i]]
      if i == len(lst) - 1:
        return res[::-1]
  return get_items_at(lst, par, res)

