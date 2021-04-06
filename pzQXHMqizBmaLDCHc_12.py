
def calculate_damage(your_type, opponent_type, attack, defense):
  i = 50 * (attack/defense)
  if your_type == 'fire':
    if opponent_type == 'grass' or opponent_type == 'fire':
      i*=2
    elif opponent_type == 'water':
      i*=0.5
  if your_type == 'grass':
    if opponent_type == 'water':
      i*=2
    elif opponent_type == 'fire':
      i*=0.5
  if your_type == 'water':
    if opponent_type == 'fire':
      i*=2
    elif opponent_type == 'grass' or opponent_type == 'electric':
      i*=0.5
  if your_type == 'electric':
    if opponent_type == 'water':
      i*=2
  return i

