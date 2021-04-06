
def join(lst,m=-1):
  if len(lst)==1: return [lst[0],m]
  for k in range(min(len(lst[0]),len(lst[1])),0,-1):
    if lst[0][-k:] == lst[1][:k]:
      lst[0:2] = [lst[0][:-k]+lst[1]]
      return join(lst,k if m==-1 else min(m,k))
  lst[0:2] = [lst[0]+lst[1]]
  return join(lst,0)

