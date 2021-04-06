
def sort_contacts(names, sort):
  if names is None:
    return []
  if len(names) == 1:
    return names
  listNames = []
  for x in names:
    y = x.split(' ')
    listNames.append(y[1])
  if sort == 'ASC':
    reverser = False
  else:
    reverser = True
  listNames.sort(reverse=reverser)
​
  ret = []
​
  for z in listNames:
    for a in names:
      if z in a:
        ret.append(a)
  return ret
#The most okay-est solution I've written.

