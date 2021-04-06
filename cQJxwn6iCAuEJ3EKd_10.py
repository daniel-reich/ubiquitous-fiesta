
def digits_count(num):
  return 1 + digits_count(num/10) if abs(num) > 9 else 1

