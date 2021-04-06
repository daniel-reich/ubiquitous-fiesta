
def split_bunches(bunches):
  return [{'name': bunch['name'], 'quantity': 1} 
    for bunch in bunches 
    for _ in range(bunch['quantity'])]

