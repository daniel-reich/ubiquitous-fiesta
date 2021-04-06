
def safecracker(start, increments):
  def dial(x):
    while True:
      y = yield x % 100
      x -= y
      y = yield x % 100
      x += y
      
  g = dial(start)
  g.send(None)
  
  return list(map(lambda x: g.send(x), increments))

