
def intersection_union(lst1, lst2):
  
  intList = []
​
  unionList = []
​
  linkedLists = lst1 + lst2
​
  for i in lst1:
      if i in lst2 and i not in intList:
          intList.append(i)
​
  for i in linkedLists:
      if i not in unionList:
          unionList.append(i)
​
  return [sorted(intList), sorted(unionList)]

