
def fizz_buzz(maximum):
  lst = []
  for x in range(1, maximum+1):
    if x % 3 == 0 and x % 5 != 0:
      lst.append("Fizz")
    elif x % 5 == 0 and x % 3 != 0:
      lst.append("Buzz")
    elif x % 5 == 0 and x % 3 == 0:
      lst.append("FizzBuzz")
    else:
      lst.append(x)
  return lst

