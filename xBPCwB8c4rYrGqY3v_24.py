
def missing(lst):
  diff = []
  for i in range(len(lst)-1):
    diff.append(lst[i+1]-lst[i])
  return lst[diff.index(max(diff))]+min(diff)

