
def is_apocalyptic(number):
  return ['Safe','Single','Double','Triple'][str(2**number).count('666')]

