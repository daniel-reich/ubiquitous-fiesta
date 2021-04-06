
def fibonacciSequence():
    l = [0,1]
    while l[-2] + l[-1] < 255:
      l.append(l[-2] + l[-1])
    return l

