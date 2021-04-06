
def multiplicity(lst):
  mylist = []
  for i in range (len(lst)):
    if [lst[i],lst.count(lst[i])] not in mylist:
      mylist.append([lst[i],lst.count(lst[i])])
  return mylist

