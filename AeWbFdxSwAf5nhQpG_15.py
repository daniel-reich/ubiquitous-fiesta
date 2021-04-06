
def persistence(num):
  counter = 0
  str_num = str(num)
  
  while len(str_num) > 1:
    prod = 1
    for d in str_num:
      prod *= int(d)
    str_num = str(prod)
    counter += 1
  
  return counter

