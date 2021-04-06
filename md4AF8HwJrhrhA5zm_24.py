
colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
sets = {"complementary" : [6], "analogous": [1, -1],
        "triadic": [4, -4], "split_complementary": [5, -5],
        "rectangle": [2, -4, 6], "square": [-3, 3, 6]}
def colour_harmony(anchor, combination):
  ind = colours.index (anchor)
  return set ([anchor] + [colours[(ind+a)%12] for a in sets[combination]])

