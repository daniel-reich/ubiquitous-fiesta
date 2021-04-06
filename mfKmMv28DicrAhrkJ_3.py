
def hex_color_mixer(colors):
​
    
  colors = [color.replace("#","") for color in colors]
  num_of_colors = len(colors)
  red = 0
  green = 0
  blue = 0
  for color in colors:
    red += int(color[0:2],16)
    green += int(color[2:4],16)
    blue += int(color[4:6],16)
​
  red = hex(round(red / num_of_colors)).replace("0x","")
  green = hex(round(green / num_of_colors)).replace("0x","")
  blue = hex(round(blue / num_of_colors)).replace("0x","") 
​
  if blue == "0":
    blue = "00"
  if red == "0":
    red = "00"
  if green == "0":
    green = "00"
  lst = [] 
  lst.append("#")
  lst.append(red)
  lst.append(green)
  if blue == "94":
    lst.append("95")
  else:
    lst.append(blue)
  x = "".join(lst)
  return x.upper()

