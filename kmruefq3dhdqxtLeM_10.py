
def sum_digits(a, b):
  sum = 0
  for i in range(a, b + 1):
    for digit in str(i):
      sum += int(digit)
  return sum
  # for j in range(0, len(str(i))):
  #   print(i[0])
  #return sum

