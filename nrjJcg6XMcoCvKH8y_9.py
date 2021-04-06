
def validate_subsets(subsets, my_set):
  lst = []
  for i in range(len(subsets)):
    for j in range(len(subsets[i])):
      lst.append(subsets[i][j])
  for i in range(len(lst)):
    if lst[i] not in my_set:
      return False 
  return True

