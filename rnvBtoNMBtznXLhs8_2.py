
def win_round(you, opp):
  highest = lambda x: int(''.join(map(str, sorted(x, reverse=True)[:2])))
  return highest(you) > highest(opp)

