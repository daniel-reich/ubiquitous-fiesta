
def check(lst):
  if all (lst[i+1]>lst[i] for i in range(len(lst)-1)): return "increasing"
  if all (lst[i+1]<lst[i] for i in range(len(lst)-1)): return "decreasing"
  return "neither"

