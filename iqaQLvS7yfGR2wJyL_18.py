
def num_of_digits(num):
  if num != 0:
    num = abs(num)
    count = 0
    while(num>0):
      num = num//10
      count += 1
    return count
  else:
    return 1

