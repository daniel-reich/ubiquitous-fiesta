
def tallest_building_height(lst):
  count = sum(1 for string in lst if "#" not in string)
  return str((len(lst)- count)*20) + 'm'

