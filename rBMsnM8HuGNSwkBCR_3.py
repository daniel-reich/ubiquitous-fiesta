
def add_bill(m):
  return sum([eval(i[1:].replace("k", "*1000")) for i in m.split(",") if "d" in i])

