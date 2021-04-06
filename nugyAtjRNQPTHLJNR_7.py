
def pages_in_book(total):
  sum_total = 0
  num = 1
  while sum_total <= total:
    sum_total += num
    num +=1
  if sum_total - (num - 1) == total:
    return True
  else:
    return False

