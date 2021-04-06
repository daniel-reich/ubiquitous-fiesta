
def error(n):
  adict = {1: 'Check the fan: e1', 2: 'Emergency stop: e2', 3: 'Pump Error: e3',4: 'c: e4', 5: 'Temperature Sensor Error: e5'}
  if n not in adict.keys():
    return 101
  else:
    return adict[n]

