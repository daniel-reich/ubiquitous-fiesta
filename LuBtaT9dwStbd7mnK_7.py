
def tallest_building_height(lst):
  a = 0
  for i in lst:
    if '#' in i:
      a += 1
    else:
      pass
  return str(a * 20) + "m"

