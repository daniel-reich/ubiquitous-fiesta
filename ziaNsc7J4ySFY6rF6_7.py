
def will_fit(holds, cargo):
  return sum({"S" : 50, "M" : 100, "L" : 200}[size] for size in holds) >= sum(cargo)

