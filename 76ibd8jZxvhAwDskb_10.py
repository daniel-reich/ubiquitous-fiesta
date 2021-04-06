
def tallest_skyscraper(list_array):
  city_length = len(list_array[0])
  buildings = {}
  for i in range(city_length):
    height = 0
    for level in list_array:
      height += level[i]
    buildings[i] = height
​
  highest_building = 0
  max_height = 0 
  for building, height in buildings.items():
    if height > max_height:
      highest_building = building
      max_height = height
​
  return max_height

