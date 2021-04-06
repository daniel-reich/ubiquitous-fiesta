
def is_narcissistic(n):
  total = 0
  num_str = str(n)
  power_exp = len(num_str)
  num_lst = []
  for num in num_str:
    exp = int(num) ** power_exp 
    num_lst.append(exp)
  
  for i in range(len(num_lst)):
    total += num_lst[i]
  
  if n == total:
    return True
  else:
    return False

