
def tallest_building_height(lst):
  lst = [item for item in lst if "#" in item]
  return str(len(lst) * 20) + "m"

