
def digits_count(num):
  if num == num % 10:
    return 1
  return 1 + digits_count(abs(num * 10 ** -1))

