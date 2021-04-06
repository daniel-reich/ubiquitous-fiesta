
def majority_vote(lst):
  max_value, majotity_vote = 0, None
  for k,v in {k: lst.count(k) for k in lst}.items(): 
    if v > max_value: max_value = v; majotity_vote = k
    elif v == max_value: majotity_vote = None
  return majotity_vote

