
def fizz_buzz(maximum):
  return ["FizzBuzz"[i % -3 & -4 : i % -5 & 8 ^ 12] or i for i in range(1, maximum + 1)]

