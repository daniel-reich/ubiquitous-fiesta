
def is_pandigital(n):
  nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  return 0 not in [c in str(n) for c in nums]

