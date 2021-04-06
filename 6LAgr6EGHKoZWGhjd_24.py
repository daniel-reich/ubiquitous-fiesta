
def final_direction(initial, turns):
  dir_list = ['N', 'E', 'S', 'W']
  start = dir_list.index(initial)
  start += sum([1 if i == 'R' else -1 for i in turns])
  return dir_list[start % 4]

