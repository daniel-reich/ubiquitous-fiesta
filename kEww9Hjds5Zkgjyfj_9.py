
def replace_next_largest(lst):
  l = sorted(lst)
  d = {k:v for k,v in zip(l,l[1:])}
  d[l[-1]] = -1
  return [d[n] for n in lst]

