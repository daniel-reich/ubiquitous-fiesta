
def direction(lst):
  newlist = []
  for eachword in lst:
    newlist.append(eachword.replace('e','w').replace('a','e').replace('E','W').replace('A','E'))
  return newlist

