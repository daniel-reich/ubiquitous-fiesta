
def simple_check(a, b):
  min_num = min(a, b)
  max_num = max(a, b)
  count = 0
  while min_num > 0:
    if max_num % min_num == 0:
      count +=1
    min_num -= 1
    max_num -= 1
  return count

