
def colour_harmony(anchor, combination):
  colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
  idx=colours.index(anchor)
  if combination=='complementary':idx=[idx,(idx+6)%12]
  elif combination=='analogous':idx=[idx,(idx-1)%12,(idx+1)%12]
  elif combination=='triadic':idx=[idx,(idx+4)%12,(idx-4)%12]
  elif combination=='split_complementary':idx=[idx,(idx+7)%12,(idx+5)%12]
  elif combination=='rectangle':idx=[idx,(idx+2)%12,(idx+6)%12,(idx+8)%12]
  elif combination=='square':idx=[idx,(idx+3)%12,(idx+6)%12,(idx+9)%12]
  return {colours[i] for i in idx}

