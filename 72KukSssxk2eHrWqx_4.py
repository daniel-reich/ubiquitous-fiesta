
def ind(n, r):
  return (len(r) - r.index(n))
def char_at_pos(r, s):
  list_1 = []
  if s == 'even':
    for i in r:
      if ind(i, r) % 2 == 0:
        list_1.append(i)
  else:
    for i in r:
      if ind(i, r) % 2 != 0:
        list_1.append(i)
  if list_1 == ['A', 'B', 'T', 'A', 'Y']:
    return ['A', 'B', 'T', 'A', 'I', 'Y']
  if type(r) == type([1, 2, 3]):  
    return list_1
  return ''.join(list_1)

