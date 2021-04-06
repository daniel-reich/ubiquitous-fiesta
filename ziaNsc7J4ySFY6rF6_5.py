
def will_fit(holds, cargo):
  d = {"S": 50, "M": 100, "L": 200}
  y = [d[i] for i in holds]
  return sum(y) > sum(cargo)

