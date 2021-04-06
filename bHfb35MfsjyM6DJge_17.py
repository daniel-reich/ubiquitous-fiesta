
def route_diff(directions):
  csouth = directions.count('S')
  cnorth = directions.count('N')
  ceast = directions.count('E')
  cwest = directions.count('W')
  return 2*min(csouth,cnorth)+2*min(ceast,cwest)

