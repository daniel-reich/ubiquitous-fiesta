
def valid_color (color):
  if color[:4] == "rgba":
    colorrange = color[5:-1]
    listcolors = colorrange.split(",")
    count = 0
    for i in listcolors[:-1]:
      if "%" in i:
        if float(i[:-1]) >= 0 and float(i[:-1]) <= 100:
          count += 1
      else:
        if float(i) >= 0 and float(i) <= 255:
          count += 1
    if float(listcolors[-1]) >= 0 and float(listcolors[-1]) <= 1:
      count += 1
    return count == 4
  elif color[:3] == "rgb":
    #do things for rgb specific
    if " (" in color:
      return False
    else:
      colorrange = color[4:-1]
      listcolors = colorrange.split(",")
      count = 0
      for i in listcolors:
        if i == "":
          return False
        elif "%" in i:
          if float(i[:-1]) >= 0 and float(i[:-1]) <= 100:
            count += 1
        elif float(i) >= 0 and float(i) <= 255:
          count += 1
      return count == 3

