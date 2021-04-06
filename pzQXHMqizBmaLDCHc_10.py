
def calculate_damage(your_type, opponent_type, attack, defense):
  supereffective = [('fire','grass'), ('grass','water'), ('water','fire'), ('electric','water')]
  neutral = [('fire','electric'), ('grass','electric'), ('electric', 'fire'), ('electric','grass')]
  
  effectiveness = 0.5
  if (your_type,opponent_type) in supereffective:
    effectiveness = 2
  elif (your_type,opponent_type) in neutral:
    effectiveness = 1
    
  return 50 * (attack / defense) * effectiveness

