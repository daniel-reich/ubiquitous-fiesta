
def count_towers(towers):
  y = []
  for i in towers:
    for j in i:
      x = j.count("##")
      y.append(x)
  return max(y)

