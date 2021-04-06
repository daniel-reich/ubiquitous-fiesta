
def compound_interest(p, t, r, n):
  interest = (p*(1+(r/n))**(n*t))
  return round(interest, 2)

