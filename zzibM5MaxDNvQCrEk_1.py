
sizes = {'S':50,'M':100,'L':200}
def will_fit(holds, cargo):
  totalSpace = 0
  totalCargo = 0
  for i in holds: totalSpace+= sizes[i];
  for i in cargo: totalCargo += i
  return totalCargo <= totalSpace

