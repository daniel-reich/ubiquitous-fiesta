
def add_str_nums(num1, num2):
  if any([l.isalpha() for l in num1]) or any([l.isalpha() for l in num2]): return '-1'
  return str(change_num(num1) + change_num(num2))
 
def change_num(num):
  if num == "" : return 0
  for i,n in enumerate(num):    
    if n != "0":
      num = num[i:]
      break
  return int(num)

