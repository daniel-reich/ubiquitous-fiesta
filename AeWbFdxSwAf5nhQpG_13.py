
def persistence(num):
  count = 0
  sum = 1
  while len(str(num)) > 1:  
    count += 1
    num = str(num)
    for i in num:
      sum *= int(i)
    num = sum
    sum = 1
  return count

