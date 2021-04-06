
def two_digit_sum(n):
  
  ten_digit = lambda num: num // 10
  one_digit = lambda num: num % 10
  
  return sum([ten_digit(n), one_digit(n)])

