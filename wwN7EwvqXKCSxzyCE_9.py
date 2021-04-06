
def reorder_digits(lst, direction):
  l = []
  if direction  == 'asc':
    for i in lst:
      i = str(i)
      i = list(i)
      i = sorted(i)
      l.append(int(''.join(i)))
  else:
    for i in lst:
      i = str(i)
      i = list(i)
      i = sorted(i,reverse = True)
      l.append(int(''.join(i)))
  return l

