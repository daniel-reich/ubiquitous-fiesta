
def digits(number):
  num = number
  s = str(number)
  total = 0
  for i in range(len(s)):
    total += int(9 * i * 10 ** (i - 1))
  total += ((num - 10 ** (len(s) - 1)) * len(s))
  return total

