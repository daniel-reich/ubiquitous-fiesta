
def calculate_damage(your_type, opponent_type, attack, defense):
  eff = (("fire", "grass"), ("water", "fire"), ("grass", "water"), ("electric", "water"))
  if (your_type, opponent_type) in eff:
    effectiveness =  2
  elif (opponent_type, your_type) in eff:
    effectiveness = 0.5
  else:
    effectiveness = 1
  return 50 * (attack / defense) * effectiveness

