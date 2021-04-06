
def calculate_damage(your_type, opponent_type, attack, defense):
  e = {('fire', 'grass'): 2,
      ('fire', 'water'): .5,
      ('fire', 'electric'): 1,
      ('water', 'grass'): .5,
      ('water', 'electric'): .5,
      ('grass', 'electric'): 1,
      ('fire', 'fire'): .5}
  effectiveness = e.get((your_type,opponent_type),0) or 1/e.get((opponent_type,your_type)) 
  return 50 * (attack / defense) * effectiveness

