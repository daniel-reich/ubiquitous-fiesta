
tax = .06
def checkout(cart):
  total = 0
  for item in cart:
    cost = item["prc"] * item["qty"]
    if item["taxable"] == True:
      cost += (cost * tax)
    total += cost
  return round(total,2)

