
def error(n):
    d = {1:"Check the fan",2:"Emergency stop", 3:"Pump Error", 4:"c", 5:"Temperature Sensor Error"}
    return d[n] + ": e{}".format(n) if n>=1 and n <= 5  else 101

