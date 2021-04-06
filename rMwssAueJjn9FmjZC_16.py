
def number_pairs(txt):
  number = int(txt.split(' ')[0])
  rest = txt.split(' ')[1:]
  newlist = sorted(list([int(x) for x in rest]))
  newlist2 = []
  for eachnumber in newlist:
    if newlist.count(eachnumber) > 1:
      newlist2.append(1)
      x = newlist.index(eachnumber)
      del newlist[x]
      x = newlist.index(eachnumber)
      del newlist[x]
  for eachnumber in newlist:
    if newlist.count(eachnumber) > 1:
      newlist2.append(1)
      x = newlist.index(eachnumber)
      del newlist[x]
      x = newlist.index(eachnumber)
      del newlist[x]
  return sum(newlist2)

