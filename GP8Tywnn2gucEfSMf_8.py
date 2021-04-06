
def error(n):
  return {1: "Check the fan: e1",2: "Emergency stop: e2", 3: "Pump Error: e3", 4: "c: e4",5: "Temperature Sensor Error: e5"}[n] if (0 < n < 6) else 101

