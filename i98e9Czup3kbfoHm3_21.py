
def text_to_number_binary(txt):
  split_text = txt.lower().split()
  a = '' 
  for each in split_text:
    if each == 'zero':
      a += '0'
    if each == 'one':
      a += '1'
  b = (len(a))//8
  c = 8
  d = c*b
  return a[:d]

