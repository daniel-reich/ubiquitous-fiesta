
def sum_digits(a, b):
  def digit_sum(number):
    return sum([int(digit) for digit in str(abs(number))])
  return sum([digit_sum(number) for number in range(a,b+1)])

