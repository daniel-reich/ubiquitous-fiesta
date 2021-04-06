
def persistence(num, step=0):
  from functools import reduce
  while num > 9 or num < 0:
    num_list = [int(x) for x in str(num)]
    num = reduce((lambda x, y: x * y), num_list)
    step += 1
  return step

