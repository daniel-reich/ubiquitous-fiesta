
def final_direction(initial, turns):
  cardinal = ['N','E','S','W']
  change = sum(1 if turn == 'R' else -1 for turn in turns)
​
  return cardinal[(cardinal.index(initial) + change)%4]

