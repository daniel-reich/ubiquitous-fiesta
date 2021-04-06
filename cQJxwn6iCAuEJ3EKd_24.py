
def digits_count(num):
  return abs(num) < 10 or 1 + digits_count(abs(num)//10)

