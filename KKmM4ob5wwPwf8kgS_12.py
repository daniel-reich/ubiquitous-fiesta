
def get_frequencies(lst):
  myDict = {}
  mySet = set(lst)
  for x in mySet:
    myDict.update({x : lst.count(x)})
  return myDict

