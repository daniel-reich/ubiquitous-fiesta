
colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
​
def colour_harmony(anchor, combination):
  global colours
  ndx = colours.index(anchor)
  res = [ndx]
​
  if combination == 'complementary':
    res.append(ndx+6)
  elif combination == 'analogous':
    res.append(ndx+1)
    res.append(ndx-1)
  elif combination == 'triadic':
    res.append(ndx+4)
    res.append(ndx+8)
  elif combination == 'split_complementary':
    comp = (ndx+6)
    res.append(comp+1)
    res.append(comp-1)
  elif combination == 'rectangle':
    comp = (ndx+6)
    res.append(ndx+2)
    res.append(comp)
    res.append(comp+2)
  elif combination == 'square':
    res.append(ndx+3)
    res.append(ndx+6)
    res.append(ndx+9)
​
  return set(colours[i%12] for i in res)

