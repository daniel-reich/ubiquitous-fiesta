
def is_apocalyptic(n):
  apo = {0: 'Safe', 1: 'Single', 2: 'Double', 3: 'Triple'}
  return apo[str(2**n).count('666')]

