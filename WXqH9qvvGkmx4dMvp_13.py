
def fizz_buzz(num):
  if num%3==0 and num%5!=0: return 'Fizz'
  elif num%3!=0 and num%5==0: return 'Buzz'
  elif num%15==0: return 'FizzBuzz'
  else: return str(num)

