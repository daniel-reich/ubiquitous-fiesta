
def fizz_buzz(num):
  if not num%15:
    return 'FizzBuzz'
  if not num%3:
    return 'Fizz'
  if not num%5:
    return 'Buzz'
  return str(num)

