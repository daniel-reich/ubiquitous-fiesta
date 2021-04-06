
def is_positive_dominant(lst):
  pos = set([n for n in lst if n > 0])
  neg = set([n for n in lst if n < 0])
  return len(pos) > len(neg)

