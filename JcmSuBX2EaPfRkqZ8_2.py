
def get_total_price(g): 
  return round(sum([g[i]["quantity"] * g[i]["price"] for i in range(len(g))]),1)

