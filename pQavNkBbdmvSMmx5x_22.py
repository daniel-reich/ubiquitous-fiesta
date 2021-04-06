
def majority_vote(lst):
  for a in lst:
    if lst.count(a) > len(lst)/2:
      return a

