
def is_checkerboard(lst):
  if len(lst)<3: return all([abs(x.count(0)-x.count(1))<2 for x in lst])
  l=[x for y in lst for x in y]
  return all(l[i]!=l[i+1] for i in range(len(l)-1))

