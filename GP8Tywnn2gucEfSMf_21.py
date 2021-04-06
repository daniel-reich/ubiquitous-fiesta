
def error(n):
  dic={1:"Check the fan: e1",2:"Emergency stop: e2",3:"Pump Error: e3",4:"c: e4",5:"Temperature Sensor Error: e5"}
  return dic[n] if n in dic else 101

