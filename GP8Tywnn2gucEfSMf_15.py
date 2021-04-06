
def error(n):
  err={1:"Check the fan",2:"Emergency stop",3:"Pump Error",4:"c",5:"Temperature Sensor Error"}
  return err[n]+': e%d' %(n) if n in err.keys() else 101

