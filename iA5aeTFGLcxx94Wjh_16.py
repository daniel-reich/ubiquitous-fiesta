
def delete_occurrences(lst, num):
  list1=lst
  list2 = []
  revlist  = list1[::-1]
  number = num
  for k in list1:
    while list1.count(k) > number:
      getindex = revlist.index(k)
      revlist.pop(getindex)
      list1 = revlist[:]
​
  return (list1[::-1])

