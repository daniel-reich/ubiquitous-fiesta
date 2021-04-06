
def add_bill(money):
  return sum(int(m[1:]) for m in money.replace("k", "000").split(",") if m[0] == "d")

