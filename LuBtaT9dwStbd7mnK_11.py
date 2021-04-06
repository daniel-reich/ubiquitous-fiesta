
def tallest_building_height(lst):
  for idx, row in enumerate(lst):
    if '#' in row:
      return str((len(lst) - idx) * 20) + 'm'

