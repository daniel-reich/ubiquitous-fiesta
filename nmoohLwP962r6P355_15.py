
def straight_digital(n):
  if n<100: return "Not Straight"
  difs = list(set([int(str(n)[i+1]) - int(str(n)[i]) for i in range(len(str(n))-1)]))
  if len(difs)>1: return "Not Straight"
  if difs[0]==0: return "Trivial Straight"
  return difs[0]

