
tax = .06
def checkout(cart):
  return sum(i["prc"]*i["qty"] if i["taxable"]==False else (i["prc"]*i["qty"]) + (i["prc"]*i["qty"])*tax for i in cart)

