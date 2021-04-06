
def majority_vote(lst):
  if lst==[]:
    return None
  else:
    for elem in lst:
      occurence=lst.count(elem)
      if occurence>(len(lst)/2):
        return elem
    #no majority found
    return None

