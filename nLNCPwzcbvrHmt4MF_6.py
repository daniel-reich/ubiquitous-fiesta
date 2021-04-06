
def fibonacciSequence():
  a = 0
  b = 1
  c = 0
  sequence = [0, 1,]
  while not b == 233:
    c = b + a
    sequence.append(c)
    ###
    a = c + b
    sequence.append(a)
    ###
    b = a + c
    sequence.append(b)
  return sequence

