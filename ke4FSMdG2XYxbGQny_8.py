
def even_odd_transform(lst, n):
  newlist = []
  for i in lst:
    if i % 2 == 0:
      x = i - 2 * n
      newlist.append(x)
    else:
      x = i + 2 * n
      newlist.append(x)
      
  return newlist

