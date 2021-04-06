
def persistence(num):
  step = 0
  while len(str(num)) > 1 or num == 10 or num == 11:
    y = [int(i) for i in str(num)]
    prod = 1
    for i in y:
      prod *= i
    num = prod
    step += 1
  return step

