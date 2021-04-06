
def colour_harmony(anchor, combination):
  colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
  index = colours.index(anchor) + len(colours)
  colours = 3*colours
  
  if combination == "complementary":
    return {anchor, colours[index+6]}
  if combination == "triadic":
    return {anchor, colours[index+4], colours[index-4]} 
  if combination == "rectangle":
    return {anchor, colours[index+2], colours[index+6], colours[index+8]}   
  if combination == "analogous":
    return {anchor, colours[index+1], colours[index-1]}   
  if combination == "split_complementary":
    return {anchor, colours[index+5], colours[index-5]} 
  if combination == "square":
    return {anchor, colours[index+3], colours[index+6], colours[index+-3]}

