
def binary_to_decimal(binary):
  sum_integer = 0
  power = (len(binary) - 1)
  i = 0
  while power >= 0 and i <= (len(binary) - 1):
    if binary[i] == 1:
      sum_integer += (2 ** power)
      power -= 1
      i += 1
    else:
      sum_integer += 0
      power -= 1
      i += 1
  return sum_integer

