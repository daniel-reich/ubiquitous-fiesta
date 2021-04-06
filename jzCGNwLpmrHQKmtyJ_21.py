
def parity_analysis(num):
  return num % 2 == 0 and sum([int(i) for i in str(num)]) % 2 == 0 or num % 2 and sum([int(i) for i in str(num)]) % 2

