
def chi_squared_test(data):
  tot = sum([sum(data[i]) for i in data])
  col_tot = [data['E'][0]+data['T'][0],data['E'][1]+data['T'][1]]
  row_tot = [sum(data['E']),sum(data['T'])]
  edabitin = [round((col_tot[0]*row_tot[0])/tot,2),round((col_tot[1]*row_tot[0])/tot,2)]
  tutorial = [round((col_tot[0]*row_tot[1])/tot,2),round((col_tot[1]*row_tot[1])/tot,2)]
  edabitin = [((data['E'][0]-edabitin[0])**2)/edabitin[0],((data['E'][1]-edabitin[1])**2)/edabitin[1]]
  tutorial = [((data['T'][0]-tutorial[0])**2)/tutorial[0],((data['T'][1]-tutorial[1])**2)/tutorial[1]]
  x2 = round(sum(edabitin)+sum(tutorial),1)
  if x2 > 6.6:
    return [x2, "Edabitin effectiveness = 99%"]
  elif x2 > 3.8:
    return [x2, "Edabitin effectiveness = 95%"]
  return [x2, "Edabitin is ininfluent"]

