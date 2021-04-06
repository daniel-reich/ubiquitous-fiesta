
def kix_code(addr):
  i = addr.split(", ")
  a, y = i[2].split()[:2], i[1]
  while not y[0].isdigit(): y = y[1:]
  b = [i if i.isalnum() else "X" for i in y]
  return ''.join(a+b).upper()

