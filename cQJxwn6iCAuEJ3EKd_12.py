
def digits_count(num):
  return 1 if -10<num<10 else 1 + digits_count(num // 10)

