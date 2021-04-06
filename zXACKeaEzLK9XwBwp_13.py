
def split_bunches(bunches):
  temp = lambda x: {'quantity': 1, 'name': x['name']}
  return [temp(b) for b in bunches for x in range(b['quantity'])]

