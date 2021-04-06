
def tallest_building_height(lst):
  for line in lst:
    if line.find("#") >=0:
      roof_index = lst.index(line)
      break
  return "{}m".format((len(lst)-roof_index)*20)

