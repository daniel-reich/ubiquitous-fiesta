
def fibonacci_sequence():
  i = 1
  ret = [0]
  while i < 255:
    ret.append(i)
    i = ret[-1]+ret[-2]
  return ret

