
def larger_than_right(lst):
  newlist = []
  for i in range(0,len(lst)-1):
    if max(lst[i+1::]) < lst[i]:
      newlist.append(lst[i])
  newlist.append(lst[-1])
  return newlist

