
def error(n):
  dic  = {1:"Check the fan",2:"Emergency stop",3:"Pump Error",4:"c",5:"Temperature Sensor Error"}
  return '{}: e{}'.format(dic[n],n) if n in dic else 101

