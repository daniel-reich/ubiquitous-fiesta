
def binary_to_decimal(binary):
  decimalNumber = 0
  count = 7
  for i in range(8):
    decimalNumber += binary[i]*(2**count)
    count -= 1
  return decimalNumber

