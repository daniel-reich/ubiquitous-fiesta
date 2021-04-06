
def calculate_damage(your_type, opponent_type, attack, defense):
  if your_type == "fire" and opponent_type == "grass":
    eff = 2
  elif your_type == "grass" and opponent_type == "fire":
    eff = 0.5
  elif your_type == "fire" and opponent_type == "water":
    eff = 0.5
  elif your_type == "water" and opponent_type == "fire":
    eff = 2
  elif your_type == "water" and opponent_type == "grass":
    eff = 0.5
  elif your_type == "grass" and opponent_type == "water":
    eff = 2
  elif your_type == "water" and opponent_type == "electric":
    eff = 0.5
  elif your_type == "electric" and opponent_type == "water":
    eff = 2
  else : eff = 1
​
  return 50 * (attack / defense) * eff

