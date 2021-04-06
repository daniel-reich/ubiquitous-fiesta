
def chunk(array, size):
  if size > len(array):
    return [array]
  else:
    newlist = []
    newlist2 = []
    for eachnumber in array:
      if len(newlist2) == size:
        newlist.append(newlist2)
        newlist2 = []
        newlist2.append(eachnumber)
      else:
        newlist2.append(eachnumber)
    newlist.append(newlist2)
    return newlist

