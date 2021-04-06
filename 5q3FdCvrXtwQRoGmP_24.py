
def count_towers(towers):
  tower_count =0
  for tower in towers:
    if len(tower[0].replace(' ', '')) >= tower_count:
      tower_count = len(tower[0].replace(' ', ''))
    if tower_count != 0:
      tower_count = tower_count/2
​
  return tower_count

