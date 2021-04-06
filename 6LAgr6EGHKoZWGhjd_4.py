
def final_direction(initial, turns):
  compass ="NESW"*len(turns)
  final = sum(1 if x=="R" else -1 for x in turns)
  return compass[compass.find(initial) + final]

