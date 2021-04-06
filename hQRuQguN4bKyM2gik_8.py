
def simple_check(a, b):
  count = 0
  while a != 0 or b != 0:
    bigger_num = max(a, b)
    smaller_num = min(a , b)
    try:
      if bigger_num % smaller_num == 0:
        count += 1
    except ZeroDivisionError:
      break
    a -= 1
    b -= 1
  return count

