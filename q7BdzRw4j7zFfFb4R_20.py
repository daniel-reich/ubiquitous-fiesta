
def merge_arrays(a, b):
  newlist = []
  length = min((len(a)),(len(b)))
  print(length)
  if ((len(a))==(len(b))):
    #go through a
    for x in range(len(a)):
      newlist.append(a[x])
      newlist.append(b[x])
  elif ((len(a))<(len(b))):
    #go through a
    for x in range(len(a)):
      newlist.append(a[x])
      newlist.append(b[x])
    newlist += (b[x+1:])
  else:
  #go through b
    for x in range(len(b)):
      newlist.append(a[x])
      newlist.append(b[x])
    newlist += (a[x+1:])
  return newlist

