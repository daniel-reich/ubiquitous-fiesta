
def add_bill(money):
   return sum((int(d[1:-1])*1000) if d[-1]=="k" else int(d[1:]) for d in money.split(",") if d[0]=="d")

