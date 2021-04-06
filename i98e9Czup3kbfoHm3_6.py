
def text_to_number_binary(txt):
  a=''
  for i in txt.split():
    if i.lower()=='zero': a+='0'
    elif i.lower()=='one': a+='1'
  if len(a)<8:
    return ''
  while len(a)%8!=0:
    a=a[:-1]
  return a

