
def tallest_building_height(lst):
  for i in range(len(lst)):
    if "#" in lst[i]:
      return str((len(lst)-i)*20) + "m"

