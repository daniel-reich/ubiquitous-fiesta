
def compound_interest(p,t,r,n):
  formula = p * (1 +  (r / n)) ** (n * t)
  estimate = round(formula, 2)
  return estimate

