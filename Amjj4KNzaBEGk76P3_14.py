
def chemical_reactions(carbon, hydrogen, oxygen):
  ans=[]
  if hydrogen==0 or oxygen==0:
    ans.append(0)
  elif hydrogen//2<=oxygen:
    ans.append(hydrogen//2)
    oxygen=oxygen-(hydrogen//2)
    hydrogen=hydrogen%2
  elif hydrogen//2>oxygen:
    ans.append(oxygen)
    hydrogen=hydrogen-(oxygen*2)
    oxygen=0
  if oxygen==0 or carbon==0:
    ans.append(0)
  elif oxygen//2<=carbon:
    ans.append(oxygen//2)
    carbon=carbon-(oxygen//2)
    oxygen=oxygen%2
  elif oxygen//2>carbon: 
    ans.append(carbon)
    oxygen=oxygen%2
    carbon=0
  if hydrogen==0 or carbon==0:
    ans.append(0)
  elif hydrogen//4>=carbon:
    ans.append(carbon)
  else:
    ans.append(hydrogen//4)
  return ans

