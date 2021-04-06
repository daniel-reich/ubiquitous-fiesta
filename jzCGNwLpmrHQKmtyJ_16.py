
def sum_digits(n):
  return n%10 + sum_digits(int(n/10)) if n else 0
def parity_analysis(num):
  return (sum_digits(num) % 2 == 0) == (num % 2 == 0)

