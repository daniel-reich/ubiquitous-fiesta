
def win_round(you, opp):
  y = sorted(you,reverse=True)
  o = sorted(opp,reverse=True)
  return True if int(str(y[0])+str(y[1])) > int(str(o[0])+str(o[1])) else False

