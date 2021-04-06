
def count_repetitions(lst):
  S=set(lst)
  d={}
  for x in S:
    d[x]=lst.count(x)
  A=[x for x in d.items()]
  return dict(sorted(A, key=lambda x: x[1], reverse=True))

