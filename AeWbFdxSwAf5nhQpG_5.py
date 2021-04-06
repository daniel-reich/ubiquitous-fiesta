
def persistence(num):
  if len(str(num)) == 1:
    return 0
  count = 0
  while len(str(num)) != 1:
    num_temp = 1
    for i in str(num):
      num_temp *= int(i)
    count += 1
    num = num_temp
    if len(str(num)) == 1:
      return count
  return count

