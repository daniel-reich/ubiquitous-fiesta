
def sums_up(lst):
  from itertools import combinations
  lst2 = [sorted(list(i)) for i in combinations(lst,2) if sum(i)==8]
  
  def func(x):
    (a,b) = x
    return max(lst.index(a),lst.index(b))
​
  return {'pairs':sorted(lst2,key=func)}

