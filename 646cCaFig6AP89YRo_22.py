
def fizz_buzz(n):
  return [i if (i%3)*(i%5) else 'Fizz'*(not i%3)+'Buzz'*(not i%5) for i in range(1, n+1)]

