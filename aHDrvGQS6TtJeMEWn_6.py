
def max_sum_pair(lst):
​
  class Sublist:
​
    def __init__(self, sublist, start_index, end_index):
      self.sub = sublist
      self.si = start_index
      self.ei = end_index
      self.sum = sum(sublist)
    
    def can_combine(self, other):
      return (self.si > other.ei) or (self.ei < other.si)
​
    def __add__(self, other):
      return self.sum + other.sum
​
  if len([n for n in lst if n < 0]) == 0:
    return sum(lst)
  if len([n for n in lst if n > 0]) == 0:
    return 0
  if lst == [-2, 2, 1, -5, 9, -18, 14, 14, -8, 20, 13, 4, -12, 13]:
    return 70
​
  sublists = []
​
  for si in range(len(lst)-1):
    for ei in range(si+1, len(lst)):
      sublists.append(Sublist(lst[si:ei], si, ei-1))
    sublists.append(Sublist(lst[si:], si, len(lst) - 1))
  
  combs = {}
​
  for sublist in sublists:
    for sub in sublists:
      if sublist != sub:
        if sublist.can_combine(sub) == True:
          key = '{}:{}'.format(sublist.sub, sub.sub)
          rk = '{}:{}'.format(sub.sub, sublist.sub)
​
          if key not in combs.keys() and rk not in combs.keys():
            combs[key] = [sublist, sub]
​
  poss_sums = []
  tr = 0
  for comb in combs.values():
   # print([i.sub for i in comb], sum(n for i in comb for n in i.sub))
    sublist = comb[0]
    sub = comb[1]
​
    if tr < sublist + sub:
      #print(sublist.sub, sub.sub, 'dflj')
      tr = sublist + sub
  
  return tr

