
def jazzify(lst):
  newlist = []
  for eachitem in lst:
    if eachitem[-1] == '7':
      newlist.append(eachitem)
    else:
      x = '{}7'.format(eachitem)
      newlist.append(x)
  return newlist

