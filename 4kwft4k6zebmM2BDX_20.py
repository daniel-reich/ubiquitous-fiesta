
def chi_squared_test(data):
  alpha1 = 6.635
  alpha5 = 3.841
  totalRow = 0
  totFirstCol = 0
  totSecondCol = 0
  chi_squared_val = 0
  colTotal = []
​
  # 1st step
  for key in data.keys():
    vl = list(data.get(key))
    totFirstCol += vl[0]
    totSecondCol += vl[1]
    for x in data.get(key):
      totalRow += x
    data[key].append(totalRow)
    totalRow = 0
  colTotal.append(totFirstCol)
  colTotal.append(totSecondCol)
  colTotal.append(totFirstCol + totSecondCol)
  
  # 2nd step and chi squared value calculation
  for key in data.keys():
    for j in range(len(colTotal)-1):
      val = data[key][2] * colTotal[j] / colTotal[-1]
      data[key].append(val)
  for key in data.keys():
    for i in range(2):
      data[key][i] = ((data[key][i] - data[key][i+3]) ** 2) / data[key][i+3]
      print(data[key][i])
      chi_squared_val += data[key][i]
  chi_squared_val = round(chi_squared_val,1)
  print(chi_squared_val)
​
  if(chi_squared_val > alpha1):
    return [chi_squared_val, "Edabitin effectiveness = 99%"]
  elif(alpha5 < chi_squared_val < alpha1):
    return [chi_squared_val, "Edabitin effectiveness = 95%"]
  elif(chi_squared_val < alpha5):
    return [chi_squared_val, "Edabitin is ininfluent"]

