
def findSmallestNum(lst):
  smallest=lst[0]
  for x in lst:
    if x < smallest:
      smallest = x
  return smallest

