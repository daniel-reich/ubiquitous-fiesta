
def chi_squared_test(data):
  matriz = [data["E"], data["T"]]
  for i in range(2):
    matriz[i].append(matriz[i][0] + matriz[i][1])
  matriz.append([matriz[0][0] + matriz[1][0], matriz[0][1] + matriz[1][1], matriz[0][2] + matriz[1][2]])
  
​
  M = [[0, 0]for i in range(2)]
  chi = 0
  for i in range(2):
    for j in range(2):
      M[i][j] = (matriz[i][2] * matriz[2][j]) / matriz[2][2]
      M[i][j] = ((matriz[i][j] - M[i][j])**2)/M[i][j]
      chi += M[i][j]
  
  if chi > 6.635:
    msg = "Edabitin effectiveness = 99%"
  elif  3.841 < chi < 6.635:
    msg = "Edabitin effectiveness = 95%"
  else:
    msg = "Edabitin is ininfluent"
​
  return[round(chi, 1), msg]

