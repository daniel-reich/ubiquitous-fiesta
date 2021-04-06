
def route_diff(directions):
  return (len(directions) -
  (abs(directions.count('N') - directions.count('S')) +
  abs(directions.count('W') - directions.count('E')))
  )

