
def difference_two(lst):
  def tr_sorter(tr):
    dic = {}
    
    for item in tr:
      dic[item[0]] = item
    
    tr = []
    
    for num in sorted(list(dic.keys())):
      tr.append(dic[num])
    
    return tr
    
  from itertools import permutations as p
  
  perms = list(p(lst,2))
  tr = []
  
  for perm in perms:
    diff = abs(perm[0] - perm[1])
    if diff == 2 and sorted(perm) not in tr:
      tr.append(sorted(perm))
  
  return tr_sorter(tr)

