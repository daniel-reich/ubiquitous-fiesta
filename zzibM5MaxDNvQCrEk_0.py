
def will_fit(holds, cargo):
  d={"S":50,"M":100,"L":200}
  return all(map(lambda x,y: x<=d[y],cargo,holds))

