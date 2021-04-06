
def error(n):
  d= {1: "Check the fan",2: "Emergency stop",3: "Pump Error",
      4: "c", 5: "Temperature Sensor Error"}
  return "{}: e{}".format(d[n], n) if n in d else 101

