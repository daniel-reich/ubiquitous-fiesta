
def fizz_buzz(num):
  if num % 3 < 1 and num % 5 < 1: return "FizzBuzz"
  if num % 3 < 1: return "Fizz"
  if num % 5 < 1: return "Buzz"
  return str(num)

