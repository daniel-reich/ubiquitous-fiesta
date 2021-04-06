
def error(n):
  dic = {1:"Check the fan", 2:"Emergency stop", 3:"Pump Error", 4:"c", 5:"Temperature Sensor Error"}
  if n in dic.keys():
    return dic[n] + ": e" + str(n)
  else:
    return 101

