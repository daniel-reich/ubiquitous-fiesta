
def colour_harmony(anchor, ctype):
  colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
  anchor_idx = colours.index(anchor)
  ctypes = {'complementary':[6],
            'triadic':[4,8],
            'split_complementary':[5,7],
            'square':[3,6,9],
            'analogous':[1,11],
            'rectangle':[2,6,8]}
  result = [anchor]
  for add in ctypes[ctype]:
    result += [colours[(anchor_idx+add) % 12]]
  return set(result)

