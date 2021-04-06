
def is_apocalyptic(n):
  lst = ['Safe', 'Single', 'Double', 'Triple']
  return lst[str(2**n).count('666')]

