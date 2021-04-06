
def chemical_reactions(carbon, hydrogen, oxygen):
  l=[]
  if hydrogen//2>=oxygen:
    l.append(oxygen)
    hydrogen-=2*oxygen
    oxygen=0
  else:
    l.append(hydrogen//2)
    oxygen-=hydrogen//2
    hydrogen%=2
  if oxygen//2>=carbon:
    l.append(carbon)
    oxygen-=2*carbon
    carbon=0
  else:
    l.append(oxygen//2)
    carbon-=oxygen//2
    oxygen%=2
  if hydrogen//4>=carbon:
    l.append(carbon)
    hydrogen-=4*carbon
    carbon=0
  else:
    l.append(hydrogen//4)
    carbon-=hydrogen//2
    hydrogen%=4
  return l

