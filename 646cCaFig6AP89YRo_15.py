
def fizz_buzz(maximum):
  result = []
  for i in range(1, maximum + 1):
    if not i % 5:
      if not i % 3:
        result.append("FizzBuzz")
      else: 
        result.append("Buzz")
    elif not i % 3:
      result.append("Fizz")
    else:
      result.append(i)
  return result

