
def fizz_buzz(maximum):
  b = []
  for i in range(1,maximum+1):
    if i%3 == 0 and i%5 == 0:
      a = "FizzBuzz"
      b.append(a)
    elif i%3 == 0:
      a = "Fizz"
      b.append(a)
    elif i%5 == 0:
      a = "Buzz"
      b.append(a)
    else:
      a = i
      b.append(a)
  return b

