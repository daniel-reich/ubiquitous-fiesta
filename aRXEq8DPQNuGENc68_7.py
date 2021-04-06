
def salt(t):
  kg=10.
  for i in range(t*6000):
    kg=kg+(1/60000)-((1/600)*(kg/100))
  return round(kg,3)

