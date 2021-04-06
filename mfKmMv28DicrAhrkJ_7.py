
def hex_color_mixer(colors):
  total, r, g, b = 0, 0, 0, 0
  for i in colors:  
    total += 1
    i = i.strip("#")
    i = tuple(int(i[j:j+2],16) for j in (0,2,4))
    r, g, b = r + i[0], g + i[1], b + i[2]
  r, g, b = r / total, g / total, b / total
  if r % 1 >= 0.5: r = round(r+.1)
  else: r = round(r)
  if g % 1 >= 0.5: g = round(g+.1)
  else: g = round(g)
  if b % 1 >= 0.5: b = round(b+.1)
  else: b = round(b)
  return "#%02x%02x%02x".upper() % (r,g,b)

