
def is_autobiographical(n):
  str_n = str(n)
  digits = "0123456789"
  
  len_n = len(str_n)
  digits = digits[:len_n]
  count_dict = dict(zip(digits, str_n))
  
  for i in range(len(digits)):
    if int(count_dict[digits[i]]) != str_n.count(digits[i]):
      return False
  return True

