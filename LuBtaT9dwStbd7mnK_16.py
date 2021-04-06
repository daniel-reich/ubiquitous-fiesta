
def tallest_building_height(lst):
  return str(20*(len(lst)-[i for i in range(len(lst)) if '#' in lst[i]][0]))+'m'

