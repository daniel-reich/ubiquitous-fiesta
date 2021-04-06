
def calculate_damage(your_type, opponent_type, attack, defense):
  
  if your_type == "fire":
    if opponent_type == "grass":
      effectiveness = 2
    elif opponent_type == "water":
      effectiveness = 0.5
    else:
      effectiveness = 1
      
  if your_type == "grass":
    if opponent_type == "fire":
      effectiveness = 0.5
    elif opponent_type == "water":
      effectiveness = 2
    else:
      effectiveness = 1
      
  if your_type == "water":
    if opponent_type == "fire":
      effectiveness = 2
    elif opponent_type == "grass":
      effectiveness = 0.5
    elif opponent_type == "electric":
      effectiveness = 0.5
    else:
      effectiveness = 1
      
  if your_type == "electric":
    if opponent_type == "water":
      effectiveness = 2
    else:
      effectiveness = 1
      
  damage = 50 * (attack / defense) * effectiveness
  
  return damage

