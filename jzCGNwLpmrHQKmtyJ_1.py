
def parity_analysis(num):
  return num % 2 == sum(int(i) for i in str(num)) % 2

