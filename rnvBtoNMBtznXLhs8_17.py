
def win_round(you, opp):
  you = sorted(you)
  opp = sorted(opp)
  for i in range(len(you)):
    you[i] = str(you[i])
  one = (you[-1] + you[-2])
  for i in range(len(opp)):
    opp[i] = str(opp[i])
  two = (opp[-1] + opp[-2])
  one = int(one)
  two = int(two)
  if one > two:
    return True;
  return False;

