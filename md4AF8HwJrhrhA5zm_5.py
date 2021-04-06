
colors = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
combinations = {'complementary': (0, 6),
  'analogous': (0,1,11),
  'triadic' : (0, 4, 8),
  'split_complementary' : (0, 5, 7),
  'rectangle': (0, 2, 6, 8),
  'square': (0, 3, 6, 9)
}
def colour_harmony(anchor, combination):
  index = colors.index(anchor)
  return {colors[(index+x)%12] for x in combinations[combination]}

