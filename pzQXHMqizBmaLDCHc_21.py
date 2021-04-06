
def calculate_damage(your_type, opponent_type, attack, defense, mod=1):
  effectiveness = {
    'fire':{'effective':['grass'],'ineffective':['water','fire']},
    'water':{'effective':['fire'],'ineffective':['grass','electric','water']},
    'grass':{'effective':['water'],'ineffective':['fire','grass']},
    'electric':{'effective':['water'],'ineffective':['electric']}}
​
  if opponent_type in effectiveness[your_type]['effective']: mod *= 2
  elif opponent_type in effectiveness[your_type]['ineffective']: mod /= 2
  return round(50 * (attack/defense) * mod)

