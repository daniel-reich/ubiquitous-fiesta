
def round_number(num, n):
  l = (num//n)*n
  h = (num//n + 1)*n
  return l if abs(num - l) < abs(num - h) else h

