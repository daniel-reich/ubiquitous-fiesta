
def convert_to_decimal(perc):
  newlst = []
  for i in range(len(perc)):
    newlst.append(0.01*(float(perc[i][:-1])))
  return newlst

