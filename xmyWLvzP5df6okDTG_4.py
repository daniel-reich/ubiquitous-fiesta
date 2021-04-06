
def binary_to_decimal(binary):
  binary.reverse()
  powers = range(len(binary))
  answer = 0
  for bin, power in zip(binary, powers):
    if bin == 1:
      answer += 2**power
  return answer

