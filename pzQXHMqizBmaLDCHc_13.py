
def calculate_damage(your_type, opponent_type, attack, defense):
  me = your_type
  he = opponent_type
  r = 1
  if me == he:
    r = 1
  elif me == "water":
    if he == "fire":
      r = 2
    else:
      r = 0.5
  elif me == "fire":
    if he == "grass":
      r = 2
    elif he == "electric":
      r = 1
    else:
      r = 0.5
  elif me == "grass":
    if he == "water":
      r = 2
    elif he == "electric":
      r = 1
    else:
      r = 0.5
  return 50 * attack / defense * r

