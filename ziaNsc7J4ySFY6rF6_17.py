
def will_fit(holds, cargo):
  cargos = {"S":50, "M":100, "L":200}
  return sum([cargos[i] for i in holds]) >= sum(cargo)

