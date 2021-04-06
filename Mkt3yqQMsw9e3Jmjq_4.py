
def cycles(perm):
  remain = set(perm)
  result = []
  while len(remain) > 0:
    n = remain.pop()
    cycle = [n]
    while True:
      n = perm[n]
      if n not in remain:
        break
      remain.remove(n)
      cycle.append(n)
    result.append(cycle)
  return result
​
def disjoint_cycle_form(perm):
    ans = set()
    for cycle in cycles(perm):
        if len(cycle) > 1:
            ans.add(tuple(cycle))
    return ans

