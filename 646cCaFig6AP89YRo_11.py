
def fizz_buzz(maximum):
  rList = []
  for x in range(1,maximum + 1):
    if x % 3 == 0 and x % 5 != 0:
      rList.append("Fizz")
    elif x % 5 == 0 and x % 3 != 0:
      rList.append("Buzz")
    elif x % 5 == 0 and x % 3 == 0:
      rList.append("FizzBuzz")
    else:
      rList.append(x)
  return rList

