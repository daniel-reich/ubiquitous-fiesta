
def tallest_building_height(lst):
  return str(len([x for x in lst if x.count('#')])*20)+'m'

