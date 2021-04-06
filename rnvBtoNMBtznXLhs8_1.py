
def win_round(you, opp):
  return sorted(you)[:2:-1] > sorted(opp)[:2:-1]

