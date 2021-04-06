
def combinations(*items):
  result = 1
  for value in items:
    if value == 0:
      value = 1
    result *= value
  return result

