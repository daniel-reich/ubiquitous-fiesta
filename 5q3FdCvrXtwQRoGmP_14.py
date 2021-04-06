
def count_towers(towers):
  lst1 = []
  for i in range(len(towers)):
    for j in range(len(towers[i])):
      lst1.append(towers[i][j].split(" ").count("##"))
  return max(lst1)

