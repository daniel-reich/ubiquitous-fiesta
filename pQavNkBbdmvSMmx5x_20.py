
def majority_vote(lst):
  nb_votes = len(lst)
  for el in set(lst):
    if lst.count(el) > nb_votes/2:
      return el
  return None

