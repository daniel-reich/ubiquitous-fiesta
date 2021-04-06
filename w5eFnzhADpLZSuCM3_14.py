
def multiplicity(lst):
  seen = set()
  final = []
  f_a = final.append
  seen_add = seen.add
  for u in lst:
    if not u in seen: 
      f_a([u, lst.count(u)])
      seen_add(u)
  return final

