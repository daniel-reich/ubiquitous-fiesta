
def chi_squared_test(data):
  import math
  ETot = sum(data["E"])
  TTot = sum(data["T"])
  TwoTot = sum([data["E"][0], data["T"][0]])
  HalfTot = sum([data["E"][1], data["T"][1]])
  SumTot = ETot + TTot
  EEV = [(ETot * TwoTot * 1.0) / SumTot, (ETot * HalfTot * 1.0) / SumTot]
  TEV = [(TTot * TwoTot * 1.0) / SumTot, (TTot * HalfTot * 1.0) / SumTot]
  EChi = [math.pow(data["E"][0] - EEV[0],2) / EEV[0], math.pow(data["E"][1] - EEV[1], 2)/EEV[1]]
  TChi = [math.pow(data["T"][0] - TEV[0],2) / TEV[0], math.pow(data["T"][1] - TEV[1], 2)/TEV[1]]
  s = round(sum(EChi) + sum(TChi),1)
  if (s > 6.635):
    return [s, "Edabitin effectiveness = 99%"]
  elif (s > 3.841):
    return [s, "Edabitin effectiveness = 95%"]
  else:
    return [s, "Edabitin is ininfluent"]

