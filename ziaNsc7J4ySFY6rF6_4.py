
def will_fit(holds, cargo):
  
  L = 200
  M = 100
  S = 50
  
  h = 0
  
  for hold in holds:
    h += eval(hold)
  
  c = sum(cargo)
  
  return c<=h

