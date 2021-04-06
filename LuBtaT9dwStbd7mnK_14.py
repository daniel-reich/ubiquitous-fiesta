
def tallest_building_height(lst):
  count = 0
  for i in lst:
    if '#' in i:
      count += 1
  return str(count * 20) + 'm'

