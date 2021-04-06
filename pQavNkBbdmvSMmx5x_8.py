
def majority_vote(lst):
  for vote in set(lst):
    if lst.count(vote) > len(lst)/2:
      return vote
  return None

