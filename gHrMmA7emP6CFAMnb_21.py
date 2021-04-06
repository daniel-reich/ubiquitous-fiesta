
def is_apocalyptic(n):
  return {
  0: 'Safe',
  1: 'Single',
  2: 'Double',
  3: 'Triple'
  }.get(str(2**n).count('666'))

