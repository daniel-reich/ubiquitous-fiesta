
def get_frequencies(lst):
  d=dict()
  sset = set(lst)
  lst1 = list(sset)
  lst1.sort()
  for i in range (len(lst1)):
    count=lst.count(lst1[i])
    d[lst1[i]]= count
  return d

