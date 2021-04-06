
def fizz_buzz(maximum):
  lst = []
  for num in range(1, maximum+1):
    if not num % 3 and not num % 5:
      lst.append('FizzBuzz')
    elif not num % 3:
      lst.append('Fizz')
    elif not num % 5:
      lst.append('Buzz')
    else:
      lst.append(num)
  return lst

