
def parity_analysis(num):
  return num % 2 == sum([int(x) for x in str(num)]) % 2

