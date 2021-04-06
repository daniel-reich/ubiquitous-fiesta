
def left_digit(num):
  import re
  x=re.search("\d",num)
  return int(num[x.start()])

