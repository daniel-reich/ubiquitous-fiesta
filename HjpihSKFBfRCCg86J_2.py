
def compound_interest(p, t, r, n):
  # p(1 + r/n)^n*t 
  power = n*t
  ans = p * (1 + r/n)**(power) 
  return round(ans,2)

