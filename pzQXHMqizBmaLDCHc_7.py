
def calculate_damage(your_type, opponent_type, attack, defense):
  win={'fire':['water'],'grass':['fire'],'water':['grass','electric'],'electric':[]}
  if your_type in win[opponent_type]:
    effectiveness=2
  elif opponent_type in win[your_type]:
    effectiveness=0.5
  else:
    effectiveness=1
  return 50 * (attack / defense) * effectiveness

