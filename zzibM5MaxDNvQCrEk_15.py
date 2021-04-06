
def will_fit(holds, cargo):
  cs = {"S":50, "M":100, "L":200}
  return sum(cs[i] for i in holds) >= sum(cargo)

