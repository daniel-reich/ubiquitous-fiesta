
def compound_interest(p, t, r, n):
  comp = p*(1+(r/n))**(n*t)
  return round(comp,2)

