
def longest_7segment_word(lst):
  cands = sorted((w for w in lst if all(l not in w for l in "kmvwx")),key= lambda w:(len(w),-lst.index(w)))
  return cands[-1] if cands else ""

