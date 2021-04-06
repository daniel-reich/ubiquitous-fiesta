
def valid_str_number(n):
  decimal_flag = False
  for char in n:
    if char in '0123456789':
      pass
    elif char == '.':
      if decimal_flag:
        return False
      decimal_flag = True
    else:
      return False
  return True

