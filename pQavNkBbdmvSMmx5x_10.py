
def majority_vote(lst):
  if len([x for x in lst if (len(lst) / 2) < lst.count(x)]) == 0:
    return None
  return ''.join(set(x for x in lst if (len(lst) / 2) < lst.count(x)))

