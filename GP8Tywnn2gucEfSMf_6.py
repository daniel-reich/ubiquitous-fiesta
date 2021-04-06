
def error(n):
  dict = {1 : "Check the fan",
          2 : "Emergency stop",
          3 : "Pump Error",
          4 : "c",
          5 : "Temperature Sensor Error"}
  if n >5 or n<1:
    return 101
  else:
    return "{}: e{}".format(dict[n],n)

