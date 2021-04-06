
def parity_analysis(num):
  if num % 2 != 0 :
    return sum([int(i) for i in str(num)]) % 2 != 0 and num % 2 != 0
  else:
    return sum([int(i) for i in str(num)]) % 2 == 0 and num % 2 == 0

