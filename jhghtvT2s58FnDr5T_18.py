
def jazzify(lst):
  if lst == []:
    return []
  new = []
  for i in lst:
    if i[-1] == '7':
      new.append(i)
    else:
      new.append(i+'7')
  return new

