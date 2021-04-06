
def initialize(names):
  lst = []
  for row in names:
    a, b = row.split()
    lst.append(a[0] + '. ' + b[0] + '.')
  return lst

