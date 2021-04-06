
def error(n):
  d = {
    1 : "Check the fan",
    2 : "Emergency stop",
    3 : "Pump Error",
    4 : "c",
    5 : "Temperature Sensor Error"
  }
  return 101 if n < 1 or n > 5 else '{}: e{}'.format(d[n], n)

