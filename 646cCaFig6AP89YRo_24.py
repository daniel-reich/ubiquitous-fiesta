
def fizz_buzz(maximum):
  return ['FizzBuzz'  if not i%15 else 'Buzz' if not i%5 \
  else 'Fizz' if not i%3 \
  else i for i in range(1, maximum+1)]

