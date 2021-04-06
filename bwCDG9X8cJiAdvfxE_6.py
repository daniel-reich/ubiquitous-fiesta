
def add_str_nums(num1, num2):
  if num1 == '' and num2 == '':return '0'
  if num1 == '':return num2
  if num2 == '':return num1
  if num1.isdigit() and num2.isdigit():return str(int(num1) + int(num2))
  return '-1'

