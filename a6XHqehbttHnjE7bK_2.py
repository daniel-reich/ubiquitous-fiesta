
def is_repdigit(num):
  num = str(num)
  return num.count(num[0]) == len(num)

