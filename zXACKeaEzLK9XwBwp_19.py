
def split_bunches(bunches):
  new = []
  for i in bunches:
    n = i['quantity']
    i['quantity'] = 1
    for j in range(0, n):
      new.append(i)
  return new

