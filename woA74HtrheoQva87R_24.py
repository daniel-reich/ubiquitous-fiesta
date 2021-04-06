
def concat(*args):
  mylist = []
  for i in range (len(args)):
    for j in range (len(args[i])):
      mylist.append(args[i][j])
  return mylist

