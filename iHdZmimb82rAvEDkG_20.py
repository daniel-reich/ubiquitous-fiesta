
def bitwise_index(lst):
  m = -10
  index = -10
  for i in range(len(lst)):
    e = (lst[i] // 2) * 2
    if e == lst[i] and lst[i] > m:
      m = lst[i]
      index = i
  if m == -10 and index == -10: return 'No even integer found!'
  if (index // 2) * 2 != index:
    return {'@odd index ' + str(index) : m}
  else:
    return {'@even index ' + str(index) : m}

