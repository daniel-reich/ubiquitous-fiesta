
def calculate_score(games):
  s = 0
  for g in games:
    if "".join(g) in "PRSP": s+=1
    if "".join(g) in "PRSP"[::-1]: s-=1
    
  if s>0: return "Abigail"
  if s<0: return "Benson"
  return "Tie"

