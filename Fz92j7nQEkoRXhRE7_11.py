
def jumping_frog(n, stones):
  i,jumps, unresolvable_spot, bad_spaces, hyper_jump=0,1,[],[],[]
  for j in range(len(stones)):
    if(j+stones[j]<len(stones)):
      if (stones[i]==0 or stones[j+stones[j]]==0):
        bad_spaces.append(j)
    if (j+stones[j]>=len(stones) and j< len(stones)-1):
      hyper_jump.append(j)
  while i<len(stones):
    if (i+stones[i] not in bad_spaces):
      i+=stones[i]
      jumps+=1
      if (i<len(stones)-1):
        if(i-stones[i]>=0):
          if (i-stones[i] in hyper_jump):
            i-=stones[i]
            jumps+=1
            i+=stones[i]
            jumps+=1
    else:
      unresolvable_spot.append(i)
      i-=stones[i]
      jumps+=1
      if(i<0):
        return ("no chance :-(")
    if (i in unresolvable_spot):
      return ("no chance :-(")
  return jumps

