
def text_to_num(phone):
  
  s1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  s2 = '22233344455566677778889999'
  s3 = ''
  
  for l in s1:
    phone = phone.replace(l,s2[s1.index(l)])
    
  return phone

