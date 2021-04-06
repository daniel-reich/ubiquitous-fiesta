
def is_numeric(c):
  if ord(c)>=ord('0') and ord(c)<=ord('9'):
    return True
  return False
  #32..2
  #.3
  #21.22
  #fas223
  #((()))
  #??f322
  #2334.33?
  
def valid_str_number(n):
  c_count=0
  for x in n:
    if x=='.':
      if c_count==0:
        c_count = 1
      else:
        return False
    elif not is_numeric(x):
      return False
  return True

