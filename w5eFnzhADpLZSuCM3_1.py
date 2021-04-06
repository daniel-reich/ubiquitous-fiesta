
def multiplicity(lst):
  a=[]
  for item in sorted(set(lst),key=lst.index):
    a.append([item,lst.count(item)])
  return a

