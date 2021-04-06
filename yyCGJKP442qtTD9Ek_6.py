
def sums_of_powers_of_two(n):
  binary, result = bin(n)[2:], []
  for index, digit in enumerate(reversed(binary)):
    if int(digit):
      result.append(2 ** index)
  return result

