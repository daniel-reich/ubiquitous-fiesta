
def text_to_num(phone):
  f = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  s = '22233344455566677778889999'
  return phone.translate(str.maketrans(f, s))

