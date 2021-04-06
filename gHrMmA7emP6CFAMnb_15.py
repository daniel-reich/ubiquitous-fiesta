
def is_apocalyptic(n):
  c = str(2 ** n).count('666')
  return ['Safe', 'Single', 'Double', 'Triple'][c]

