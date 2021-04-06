
def win_round(you, opp):
  you = ''.join(str(i)for i in sorted(you, reverse=True))[:2]
  opp = ''.join(str(i)for i in sorted(opp, reverse=True))[:2]
  return you > opp

