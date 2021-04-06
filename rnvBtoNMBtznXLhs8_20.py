
def win_round(you, opp):
  you = ''.join(map(str, sorted(you, reverse=True)))
  opp = ''.join(map(str, sorted(opp, reverse=True)))
  return int(you[:2]) > int(opp[:2])

