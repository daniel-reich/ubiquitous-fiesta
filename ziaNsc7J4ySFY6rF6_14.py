
def will_fit(holds, cargo):
  dict = {"S":50, "M":100, "L":200}
  return sum(dict[i] for i in holds) >= sum(cargo)

