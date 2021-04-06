
def tallest_building_height(lst):
  tt_mtrx = [itm for itm in lst]
  mtrx = []
  for x in range(len(tt_mtrx[0])):
    row = []
    for y in range(len(tt_mtrx)):
      row.append(tt_mtrx[y][x])
    mtrx.append(row)
  return str(max(itm.count("#") for itm in mtrx) * 20) + "m"

