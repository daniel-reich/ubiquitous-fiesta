
def has_valid_price(p):
  return p!=None and "price" in p and ((type(p["price"]) in [int,float]) and p["price"] >= 0)

