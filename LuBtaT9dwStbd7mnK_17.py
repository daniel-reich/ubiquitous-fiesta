
def tallest_building_height(lst):
   x = len([i for i in lst if "#" in i]) * 20
   return str(x) + "m"

