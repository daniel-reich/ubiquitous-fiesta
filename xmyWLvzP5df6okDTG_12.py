
def binary_to_decimal(binary):
  total = 0
  current_exp = 7
  for num in binary:
    total += num * (2 ** current_exp)
    current_exp -= 1
  return total

