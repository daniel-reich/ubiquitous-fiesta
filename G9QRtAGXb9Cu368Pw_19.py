
def combinations(*items):
  result = 1
  for i in range(0, len(items)):
    if(items[i] != 0):
      result = result * items[i]
  return result

