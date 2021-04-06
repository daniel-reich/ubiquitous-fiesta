
def fizz_buzz(num):
  x = ""
  if num % 3 == 0:
    x = "Fizz"
  if num % 5 == 0:
    x = x + "Buzz"
  return x if x != "" else str(num)

