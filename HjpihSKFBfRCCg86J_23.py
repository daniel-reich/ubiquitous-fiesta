
def compound_interest(p, t, r, n):
  a = p*(1+r/n)**(n*t)
  return round(a, 2)

