
def colour_harmony(anchor, combination):
  colors=["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
  d={'complementary':[6],'analogous':[-1,1],'triadic':[4,-4],'split_complementary':[-5,5],'rectangle':[2,6,8],'square':[3,6,9]}
  return set([colors[(colors.index(anchor)+x)%12] for x in d[combination]]+[anchor])

