
def fibonacciSequence():
    a = 0
    b = 1
    c = 1
    x = [0, 1, 1]
    while c < 233:
      a , b = b, c
      c = a + b
      x.append(c)
    return x

