
def determine_who_cursed_the_most(d):
  me = spouse = 0
  for round in d:
    me += d[round]["me"]
    spouse += d[round]["spouse"]
  return "ME!" if me > spouse else "SPOUSE!" if me < spouse else "DRAW!"

