
def calculate_damage(your_type, opponent_type, attack, defense):
  who_beats_who = {
  'fire' : 'grass',
  'grass' : 'water',
  'electric' : 'water',
  'water' : 'fire'
  }
  
  effectiveness = 1
  if who_beats_who[your_type] == opponent_type: effectiveness *= 2
  elif who_beats_who[opponent_type] == your_type: effectiveness /= 2
  return 50 * (attack / defense) * effectiveness

