
def fizz_buzz(maximum):
  j = []
  for i in range(1, maximum + 1):
    if i % 3 == 0 and i % 5 == 0:
      j.append("FizzBuzz")
      continue
    elif i % 3 == 0:
      j.append("Fizz")
      continue
    elif i % 5 == 0:
      j.append("Buzz")
      continue
    j.append(i)
  return j

