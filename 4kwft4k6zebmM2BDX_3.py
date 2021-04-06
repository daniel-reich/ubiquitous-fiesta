
def chi_squared_test(data):
  row = [0]*len(data)
  row[0] = data["E"]
  row[1] = data["T"]
  total = sum(row[0]) + sum(row[1])
  row_tot = [0]*2
  col_tot = [0]*2
  row_tot[0] = sum(row[0])
  row_tot[1] = sum(row[1])
  col_tot[0] = row[0][0] + row[1][0]
  col_tot[1] = row[0][1] + row[1][1]
​
  tab = [[float(0),float(0)] for i in range(2)]
  new = [[float(0),float(0)] for i in range(2)]
​
  for i in range(2):
    for j in range(2):
      tab[i][j] = (row_tot[i]*col_tot[j])/total
      new[i][j] = (row[i][j]-tab[i][j])**2/tab[i][j]
​
  chi = round(sum(new[0])+sum(new[1]),1)
  
  alpha1 = 6.635
  alpha5 = 3.841
  
  if chi>alpha1:
    return([chi,"Edabitin effectiveness = 99%"])
  elif chi < alpha1 and chi > alpha5:
    return([chi,"Edabitin effectiveness = 95%"])
  else:
    return([chi,"Edabitin is ininfluent"])

