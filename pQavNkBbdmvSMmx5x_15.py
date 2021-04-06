
def majority_vote(l):
  if not l: return None 
  p = [l.count(x)/len(l) for x in list(dict.fromkeys(l))]
  return list(dict.fromkeys(l))[p.index(max(p))] if max(p) > .5 else None

