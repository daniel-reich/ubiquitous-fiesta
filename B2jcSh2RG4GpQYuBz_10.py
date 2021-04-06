
def is_valid_phone_number(txt):
  flag = True
  form = '(***) ***-****'
  nums = '0123456789'
  index = 0
  if len(form) == len(txt):
    for char in txt:
      if char in nums:
        if form[index] != '*':
          flag = False
      elif char in form:
        if form[index] != char:
          flag = False
      else:
        flag = False
      index += 1
  else:
    flag = False
  return flag

