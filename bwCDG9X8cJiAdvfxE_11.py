
def add_str_nums(num1, num2):
  if not num1:
    num1 = '0'
  if not num2:
    num2 = '0'
  if (not num1.isnumeric()) or (not num2.isnumeric()):
    return '-1'
  return str(int(num1) + int(num2))

