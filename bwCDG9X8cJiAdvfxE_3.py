
def add_str_nums(num1, num2):
  if any(ch.isalpha() for n in [num1,num2] for ch in n):
    return '-1'
  if num1 == '': num1 = 0
  if num2 == '': num2 = 0
  return str(int(num1)+int(num2))

