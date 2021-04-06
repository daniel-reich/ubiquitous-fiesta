
def is_harshad(n):
  return n % sum(int(digit) for digit in str(n)) == 0

