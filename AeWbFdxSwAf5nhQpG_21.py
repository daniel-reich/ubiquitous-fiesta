
def persistence(num):
  count = 0
  while num >= 10:
    copy, prod = num, 1
    while copy > 0:
      prod *= copy % 10
      copy //= 10
    num = prod
    count += 1
  return count

