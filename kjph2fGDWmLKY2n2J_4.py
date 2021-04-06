
def valid_color (color):
  if 'a' in color:
    colorlist = color[5:-1].split(',')
    if '' in colorlist or len(colorlist) != 4:
      return False
    colorlist = [float(i) for i in colorlist]
    a = colorlist[-1] >= 0 and colorlist[-1] <= 1
    b = all(i >= 0 and i <=255 for i in colorlist[:-1])
    return a and b
  else:
    if color.find('(') != 3:
      return False
    colorlist = color[4:-1].split(',')
    if '' in colorlist or len(colorlist) != 3:
      return False
    if '%' in colorlist[0]:
      colorlist = [int(i[:-1]) for i in colorlist]
      return all(i >= 0 and i <=100 for i in colorlist)
    colorlist = [int(i) for i in colorlist]
    return all(i >= 0 and i <=255 for i in colorlist)

