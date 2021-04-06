
def fizz_buzz(num):
  if num%3==0 and num%5==0:
    return 'FizzBuzz'
  elif num%3==0 or num%5==0:
    if num%3==0:
      return'Fizz'
    else:
      return 'Buzz'
  else:
    return str(num)

