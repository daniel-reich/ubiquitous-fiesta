
def digits_count(num):
  if abs(num) < 10:
    return 1
  return 1 + digits_count(num // 10)

