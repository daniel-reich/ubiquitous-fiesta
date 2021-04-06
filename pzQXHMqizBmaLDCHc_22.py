
def calculate_damage(your_type, opponent_type, attack, defense):
​
  types = [your_type, opponent_type]
  super_ = [
  ['fire', 'grass'],
  ['water', 'fire'],
  ['grass', 'water'],
  ['electric', 'water']
  ]
​
  not_effective = [
  ['grass', 'fire'],
  ['fire', 'water'],
  ['water', 'grass'],
  ['water', 'electric']
  ]
​
  if types in super_:
    e = 2
  elif types in not_effective:
    e = .5 
  else:
    e = 1
​
​
​
​
​
  damage = 50 * (attack // defense) * e
  return damage

