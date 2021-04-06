
def final_direction(initial, turns):
  directions = "NESW"
  return directions[(directions.find(initial) + turns.count("R") - turns.count("L")) % 4]

