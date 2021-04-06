
def will_fit(holds, cargo):
  x = holds.count("M") * 100 + holds.count("S") * 50 + holds.count("L") * 200 
  return sum(cargo) <=  x

