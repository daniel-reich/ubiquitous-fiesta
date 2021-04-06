
def choose_fuse(fuses, current):
  voltages = []
  for fuse in fuses:
    voltages.append(float(fuse[:-1]))
  voltages.sort()
  for voltage in voltages:
    if voltage >= float(current[:-1]):
      if voltage % 1 == 0:
        return str(int(voltage))+'V'
      return str(voltage)+'V'

