
def get_gcd(num1, num2):
  if num2 % num1 == 0:
    return num1
  return get_gcd(num2%num1, num1)
​
​
def GCD(lst):
  size = len(lst)
  if size == 1:
    return lst[0]
  lst.sort()
  comm_div = get_gcd(lst[0], lst[1])
  for value in lst[2:]:
    comm_div = get_gcd(comm_div, value)
  return comm_div

