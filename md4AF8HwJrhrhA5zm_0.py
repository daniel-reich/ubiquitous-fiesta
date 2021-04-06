
def colour_harmony(anchor, combination):
  colours = ['red', 'red-orange', 'orange', 'yellow-orange', 'yellow', 'yellow-green', 
         'green', 'blue-green', 'blue', 'blue-violet', 'violet', 'red-violet']
  d = {'complementary': {0, 6}, 'analogous': {-1, 0, 1}, 'triadic': {-4, 0, 4}, 
     'split_complementary': {-5, 0, 5}, 'rectangle': {-4, -6, 0, 2}, 'square': {-6, -3, 0, 3}}
  
  start, res = colours.index(anchor), set()
  for i in d[combination]:
    res.add(colours[(start + i)%12])
  return res

