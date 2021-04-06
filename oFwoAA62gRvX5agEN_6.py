
def knapsack(capacity, items):
  max_value = -float('inf')
  d = {'capacity': capacity, 'items': [], 'weight': 0, 'value': 0}
  for i in range(2**len(items)):
    items_ = [x for x, b in zip(items, format(i, '#0{}b'.format(len(items)+2))[2:]) if b=='1']
    w = sum(x['weight'] for x in items_)
    if w > capacity: continue
    v = sum(x['value'] for x in items_)
    if max_value < v:
      max_value = v
      d.update({'items': items_, 'weight': w, 'value': v})
  return d

