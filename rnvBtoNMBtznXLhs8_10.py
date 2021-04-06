
def win_round(you, opp):
  if max(you)>max(opp):
    return True
  elif max(you)==max(opp):
    if you.count(max(you))>opp.count(max(opp)):
      return True
    if max([i for i in you if i!=max(you)])>max([i for i in opp if i!=max(opp)]):
      return True
  return False

