
def first_arg(*num):
  return None if num==() else num[0]
​
def last_arg(*num):
  return None if num==() else num[-1]

