
def mean(num):
  times = len(str(num))
  numbers = list(str(num))
  result = 0
  for item in numbers:
    result += int(item)
  return result / times

