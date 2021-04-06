
def sort_nums_ascending(lst):
  newlist=list()
  for i in range(len(lst)):
    newlist.append(min(lst))
    lst.remove(min(lst))
  return newlist

