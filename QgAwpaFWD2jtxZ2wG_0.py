
def sum_digits(n):
   return 1 + sum_digits(n / 10) if n >= 10 else 1

