
def fizz_buzz(maximum):
  result = []
  for i in range(maximum):
    i = i+1
    fizz = buzz = False
    if i%3==0:
      fizz = True
    if i%5 == 0:
      buzz = True
    if fizz and buzz:
      result.append("FizzBuzz")
    elif fizz:
      result.append("Fizz")
    elif buzz:
      result.append("Buzz")
    else:
      result.append(i)
  print(result)
  return(result)

