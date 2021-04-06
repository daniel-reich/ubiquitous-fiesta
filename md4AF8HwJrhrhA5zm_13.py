
def colour_harmony(anchor, combination):
  c = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
  ind = c.index(anchor)
  if combination == 'complementary':
    return set([anchor,c[(ind+6)%12]])
  elif combination == 'analogous':
    return set([anchor,c[(ind+1)%12],c[(ind-1)%12]])
  elif combination == 'triadic':
    return set([anchor,c[(ind+4)%12],c[(ind-4)%12]])
  elif combination == 'split_complementary':
    return set([anchor,c[(ind+5)%12],c[(ind-5)%12]])
  elif combination == 'rectangle':
    return set([anchor,c[(ind+2)%12],c[(ind-4)%12],c[(ind-6)%12]])
  elif combination == 'square':
    return set([anchor,c[(ind+3)%12],c[(ind-3)%12],c[(ind-6)%12]])

