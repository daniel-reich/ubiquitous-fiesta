
def time(dct, people, walls):
  totalTime = dct['minutes'] * dct['people'] / dct['walls']
  return totalTime * walls / people

