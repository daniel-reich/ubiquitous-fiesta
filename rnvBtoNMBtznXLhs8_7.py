
def win_round(you, opp):
  return True if sorted(you)[-1]*10+sorted(you)[-2]>sorted(opp)[-1]*10+sorted(opp)[-2] else False

