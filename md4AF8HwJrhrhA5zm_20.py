
def colour_harmony(anchor, combination):
  colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
  a = colours.index(anchor)
  if combination=='complementary':
    return set([anchor, colours[(a+6)%12]])
  elif combination=='triadic':
    return set([colours[i] for i in range(len(colours)) if not (i-a)%4])
  elif combination=='square':
    return set([colours[i] for i in range(len(colours)) if not (i-a)%3])
  elif combination=='analogous':
    return set([colours[a-1], colours[a], colours[(a+1)%12]])
  elif combination=='rectangle':
    return set([colours[a],colours[(a+2)%12],colours[(a+6)%12],colours[(a+8)%12]])
  return set([colours[a],colours[(a+5)%12],colours[(a+7)%12]])

