
from statistics import median as med
def get_quartiles(lst, method):
  lst = sorted(lst)
  q0, q2, q4 = min(lst), med(lst), max(lst)
  if method == 'MS':
    v1 = (len(lst)+1)/4
    v1 = int(v1)+1 if v1%1 == 0.5 else round(v1)
    q1 = lst[v1-1]
​
    v3 = 3*(len(lst)+1)/4
    v3 = int(v3) if v3%1 == 0.5 else round(v3)
    q3 = lst[v3-1]
  else:
    ndx = len(lst)//2
    lst1, lst2 = lst[:ndx], lst[-ndx:]
    if method == 'T':
      if len(lst)%2:
        pivot = lst[len(lst)//2]
        lst1.append(pivot)
        lst2.insert(0,pivot)
    q1, q3 = med(lst1),med(lst2)
  return [q0,q1,q2,q3,q4]

