
def majority_vote(lst):
  if (len(lst) == 0):
    return None
  count = 1
  for i in range(0,len(lst)):
    for j in range(i+1, len(lst)):
      if (lst[i] == lst[j]):
        count += 1
    if (count > len(lst)/2):
      return lst[i];
    else:
      count = 1
  return None

