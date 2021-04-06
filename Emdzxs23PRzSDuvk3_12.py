
def pizza_points(cust, o, p):
  return sorted([c for c in cust if len([x for x in cust[c] if x>=p]) >= o])

