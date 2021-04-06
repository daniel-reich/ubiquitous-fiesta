
def final_direction(initial, turns):
  lst = ['N', 'E', 'S', 'W']
  turns = sum([1 if i == 'R' else -1 for i in turns])
  turns = lst.index(initial) + turns
  if turns >= 0:
    return lst[turns % 4]
  else:
    turns = -turns % 4
    return lst[-turns]

