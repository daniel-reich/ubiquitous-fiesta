
def final_direction(initial, turns):
  dir = 'NESW'
  turn = sum([1 if t=='R' else -1 for t in turns])
  return dir[(dir.find(initial)+turn)%4]

