
def letter_distance(txt_1, txt_2):
  func = lambda x: bytearray(x, encoding='utf-8')
  a = bytearray(txt_1, encoding='utf-8')
  num = 0
  
  if len(txt_1) < len(txt_2):
    b = func(txt_2)[:len(a)]
    num = len(txt_2) - len(txt_1)
  else:
    b = func(txt_2)
    
  result = sum([abs(k-v) for k, v in zip(a, b)]
          + [len(a) - len(b)])
  return result + num

