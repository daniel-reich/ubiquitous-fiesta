
def square_digits(n):
  return int(''.join([str(int(i) ** 2) for i in str(n)]))

