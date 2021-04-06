
def is_apocalyptic(number):
  apoc = {0: 'Safe', 1: 'Single', 2: 'Double', 3: 'Triple'}
  return apoc[str(2**number).count("666")]

