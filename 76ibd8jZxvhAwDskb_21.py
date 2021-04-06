
def tallest_skyscraper(list_of_height):
  skyline = len(list_of_height)
  for i in list_of_height:
    for j in i:
      if j == 1:
        return skyline - list_of_height.index(i)

