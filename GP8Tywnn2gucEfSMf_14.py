
def error(n):
  err_dict = {
    1 : "Check the fan",
    2 : "Emergency stop",
    3 : "Pump Error",
    4 : "c",
    5 : "Temperature Sensor Error",
  }
  try:
    return ("{0}: e{1}".format(err_dict[n], n))
  except:
    return 101

