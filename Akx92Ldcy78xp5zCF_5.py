
def custom_sort(t, s):
  nt =  [l8r for l8r in t if l8r in s]
  ns = []
  
  for l8r in set(s):
    if l8r in nt:
      tcount = t.count(l8r)
      scount = s.count(l8r)
      for n in range(scount - tcount):
        nt = nt[:nt.index(l8r)] + [l8r] + nt[nt.index(l8r):]
    else:
      for n in range(s.count(l8r)):
        ns.append(l8r)
  
  return ''.join(nt) + ''.join(sorted(ns))

