
def sort_by_length(lst):
  orderedDict = {}
  orderedList = []
  sorted(lst)
  for item in lst:
    orderedDict.update( {len(item) : item} )
​
  for key, value in sorted(orderedDict.items()):
    orderedList.append(value)
​
  return orderedList

