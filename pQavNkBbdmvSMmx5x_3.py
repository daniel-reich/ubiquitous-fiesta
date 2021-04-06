
def majority_vote(l):
 for e in l:
  if l.count(e)>len(l)/2:return e

