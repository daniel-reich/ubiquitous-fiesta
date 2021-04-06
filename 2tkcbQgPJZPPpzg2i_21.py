
def sum_of_holes(N):
  result = 0
  for num in range(1, N + 1):
    for digit in str(num):
      if digit in '4690':
        result += 1
      if digit == '8':
        result += 2
  return result

