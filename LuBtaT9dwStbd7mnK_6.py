
def tallest_building_height(lst):
  for i, line in enumerate(lst):
    if '#' in line:
      return '{}m'.format((len(lst) - i) * 20)

