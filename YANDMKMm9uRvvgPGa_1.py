
def same(a1, a2):
  uniqueA1 = []
  uniqueA2 = []
  
  for item in a1:
    if item not in uniqueA1:
      uniqueA1.append(item)
  for item in a2:
    if item not in uniqueA2:
      uniqueA2.append(item)
  return len(uniqueA1) == len(uniqueA2)

