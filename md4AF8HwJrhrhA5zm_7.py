
def colour_harmony(anchor, combination):
  colors = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
  aidx = colors.index(anchor) 
  spots = {
    'complementary': [0,6],
    'analogous': [-1,0,1],
    'triadic': [-4,0,4],
    'split_complementary': [-5,0,5],
    'rectangle': [-4,0,2,6],
    'square': [-3,0,3,6]
  }
​
  return set([colors[(aidx + i) % 12] for i in spots[combination]])

