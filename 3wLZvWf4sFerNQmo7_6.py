
def neutralise(s1, s2):
  lst = []
  for x in zip(s1, s2):
    if x[0] == x[1]:
      lst.append(x[0])
    else:
      lst.append('0')
  return ''.join(lst)

