
def calculate_damage(your_type, opponent_type, attack, defense):
  effectiveness=1
  d = {('fire','grass'):2,('fire','water'):0.5,('fire','electric'):1,('water', 'grass'):0.5,
         ('water', 'electric'):0.5,('grass', 'electric'):1, ('grass','fire'):0.5,("grass", "water"):2}
  for i in d:
    if i == (your_type,opponent_type):
      effectiveness=d[(your_type,opponent_type)]
  damage = 50 * (attack / defense) * effectiveness
  return damage

