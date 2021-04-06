
def win_round(you, opp):
  v=sorted(you)
  u=sorted(opp)
  m=str(v[-1])+str(v[-2])
  n=str(u[-1])+str(u[-2])
  return int(m)>int(n)

