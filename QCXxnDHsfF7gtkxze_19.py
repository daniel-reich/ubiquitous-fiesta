
def mystery_func(num):
  str_num = str(num)
  total = 1
  for i in str_num:
    total = total * int(i)
  return total

