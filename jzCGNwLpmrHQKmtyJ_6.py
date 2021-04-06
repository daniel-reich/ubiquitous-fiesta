
def parity_analysis(num):
  x = 0
  for i in str(num):
    x += int(i)
  return x % 2 == num % 2

