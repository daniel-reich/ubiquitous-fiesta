
def parity(n):
  remainder = bool(n % 2)
  if remainder == False:
    return "even"
  if remainder == True:
    return "odd"

