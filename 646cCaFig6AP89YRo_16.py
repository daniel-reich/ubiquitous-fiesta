
def fizz_buzz(maximum):
  result = []
  for num in range(1, maximum + 1):
    if num % 3 == 0 and num % 5 == 0:
      result.append("FizzBuzz")
    elif num % 3 == 0:
      result.append("Fizz")
    elif num % 5 == 0:
      result.append("Buzz")
    else:
      result.append(num)
  return result

