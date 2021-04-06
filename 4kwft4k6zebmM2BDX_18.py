
def chi_squared_test(data):
  tot = sum(data["E"]) + sum(data["T"])
  rowE = sum(data["E"])
  rowT = sum(data["T"])
  col0 = data["E"][0] + data["T"][0]
  col1 = data["E"][1] + data["T"][1]
  ex = {"E": [(rowE*col0)/tot, (rowE*col1)/tot],
              "T": [(rowT*col0)/tot, (rowT*col1)/tot]}
  chi_lst = [(data["E"][0] - ex["E"][0])**2 / ex["E"][0],
             (data["E"][1] - ex["E"][1])**2 / ex["E"][1],
             (data["T"][0] - ex["T"][0])**2 / ex["T"][0],
             (data["T"][1] - ex["T"][1])**2 / ex["T"][1]]
  chi_S = round(sum(chi_lst), 1)
  alpha1 = 6.635
  alpha5 = 3.841
  if alpha1 < chi_S:
    return [chi_S, "Edabitin effectiveness = 99%"]
  elif alpha5 < chi_S < alpha1:
    return [chi_S, "Edabitin effectiveness = 95%"]
  else:
    return [chi_S, "Edabitin is ininfluent"]

