
def time(dct, people, walls):
  rate = (dct['minutes'] * dct['people']) / dct['walls']
  return (rate * walls) / people

