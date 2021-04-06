
def BMR(p):
  f1 = {"male": [66.47, 13.75, 5.003, 6.755], "female": [655.1, 9.563, 1.85, 4.676]}[p["gender"]]
  f2 = [1.2, 1.375, 1.55, 1.725, 1.9][p["sport"] - 1]
  return round((f1[0] + f1[1] * p["weight"] + f1[2] * p["size"] - f1[3] * p["age"]) * f2, 1)

