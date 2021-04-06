
def remove_dups(l):
  s=set()
  return[x for x in l if not(x in s or s.add(x))]

