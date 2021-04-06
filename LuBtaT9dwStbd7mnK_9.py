
def tallest_building_height(lst):
  tall = 0
  for i, v in enumerate(lst):
    if "#" in v:
      tall += 1
  
  return str(20 * tall) + "m"

