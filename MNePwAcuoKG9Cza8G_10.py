
def build_staircase(height, block):
  return [[block]*i+['_']*(height-i) for i in range (1,height+1)]

