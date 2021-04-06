
def count_towers(towers):
  return int(max([towers[i][0].count("#") for i in range(0,len(towers))])/2)

