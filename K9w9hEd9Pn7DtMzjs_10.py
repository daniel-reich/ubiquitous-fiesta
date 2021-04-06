
def high_low(txt):
  return str(max(map(lambda x : int(x),txt.split(" ")))) + " " + str(min(map(lambda x : int(x),txt.split(" "))))

