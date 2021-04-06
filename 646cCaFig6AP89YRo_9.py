
def fizz_buzz(maximum):
  lst = []
  for i in range(1,maximum+1):
    lst.append(i)
  final = []
  for i in lst:
    if i%3 == 0 and i%5 != 0:
      final.append("Fizz")
    elif i%5 == 0 and i%3 != 0:
      final.append("Buzz")
    elif i%5 == 0 and i%3 == 0:
      final.append("FizzBuzz")
    else:
      final.append(i)
  return final

