
def format():
  spaces = [2, 0, 1, 0, 1, 0]
  for s in spaces:
    yield ' '  * s + '{:0' + str(4 - s) + 'b}'
    
def binary_clock(time):
  f = format()
  digits = [next(f).format(int(c)) for c in time if c != ':']
  return [''.join(row) for row in zip(*digits)]

