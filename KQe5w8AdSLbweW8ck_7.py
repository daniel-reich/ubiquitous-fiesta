
def char_at_pos(r, s):
  lst = []
  for i in range(len(r)):
    if s == 'even':
      lst.append(r[i+1::2])
    elif s == 'odd':
      lst.append(r[i::2])
  return lst[0]

