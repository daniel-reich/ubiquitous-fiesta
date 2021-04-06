
def win_round(you, opp):
  you.sort(),opp.sort()
  return str(you[-1])+str(you[-2]) > str(opp[-1])+str(opp[-2])

