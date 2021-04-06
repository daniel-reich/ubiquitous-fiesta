
def order_people(lst, people):
  if lst[0] * lst[1] < people: return 'overcrowded'
  res = []
  for row in range(lst[0]):
    direc = -1 if len(res) % 2 else 1
    res.append([n if n <= people else 0 for n in range(len(res) * lst[1] + 1, (len(res) + 1) * lst[1] + 1)][::direc])
  return res

