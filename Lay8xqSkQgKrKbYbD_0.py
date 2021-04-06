
def climbing_stairs(cost):
  if len(cost)==0:
    return cost[0]
  ans = [0]*len(cost)
  ans[-2:] = cost[-2:]
  for i in range(len(cost)-3, -1,-1):
    ans[i] = cost[i] + min(ans[i+1],ans[i+2])
  
  return min(ans[0:2])

