
def count_all(txt):
  num = "0123456789"
  str = "abcdefghijklmnopqrstuvwxyz"
  dict = {'LETTERS': 0, 'DIGITS': 0}
  #numCount = 0
  #strCount = 0
  for item in txt:
    if item in num:
      dict['DIGITS'] += 1
      #numCount += 1
    if item.lower() in str:
      dict['LETTERS'] += 1    
      #strCount += 1
  return dict

