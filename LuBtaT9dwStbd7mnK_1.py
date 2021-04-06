
def tallest_building_height(lst):
  for i in lst:
    if '#' in i:
      g=lst.index(i)
      break
  return str((len(lst)-g)*20) + 'm'

