
def split_bunches(bunches):
  return list(generator_split_bunches(bunches))
​
def generator_split_bunches(bunches):
  for bunch in bunches:
    for _ in range(bunch['quantity']):
      bunch['quantity'] = 1
      yield bunch

