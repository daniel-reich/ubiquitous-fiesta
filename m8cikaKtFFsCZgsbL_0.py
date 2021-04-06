
def waterjug(cap, goal):
  ops, que = {(0,0,cap[2]):0}, [(0,0,cap[2])]
  swaps = [(i,j) for i in [0,1,2] for j in [0,1,2]]
  while que:
    curr = que.pop(0)
    if curr == tuple(goal):
      return ops[curr]
    for i,j in swaps:
      exc = min (curr[i],cap[j]-curr[j])
      new = tuple((curr[k] - exc*(k==i) +exc*(k==j)) for k in [0,1,2])
      if new not in ops.keys():
        ops[new] = ops[curr]+1
        que = que + [new]
  return "No solution."

