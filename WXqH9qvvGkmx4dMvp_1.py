
def fizz_buzz(num):
  s = ''
  if num%3 == 0: s += 'Fizz'
  if num%5 == 0: s += 'Buzz'
  return s if s else str(num)

