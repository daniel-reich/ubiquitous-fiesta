
def greatest_impact(lst):
  n = len(lst)
  for i in range(n):
    lst[i][2] = int((10/3)*lst[i][2])
    
  comps = [sum(abs(lst[j][0]-lst[j][i]) for j in range(n)) for i in [1,2,3]]
​
  m = min(*comps)
​
  if comps.count(m)>1: return "Nothing"
  return ["Weather","Meals","Sleep"][comps.index(m)]

