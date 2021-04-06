
def advanced_sort(lst):
  r=[]
  while(len(lst)):
    p=lst[0]
    r+=[[p]*lst.count(p)]
    for i in range(lst.count(p)):
      lst.remove(p)
  return r

