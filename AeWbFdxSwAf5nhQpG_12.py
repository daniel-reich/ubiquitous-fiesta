
def persistence(num):
  diff = num
  count = 0
  while diff > 9:
    prod = 1
    for i in str(diff):
      prod *= int(i)
    diff = prod
    count += 1
  return count

