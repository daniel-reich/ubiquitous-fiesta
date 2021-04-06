
def num_of_digits(num):
  count = 1
  num = abs(num)
  while num // 10 > 0:
    num //= 10
    count += 1
  return count

