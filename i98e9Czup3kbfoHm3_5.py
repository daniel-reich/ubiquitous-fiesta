
def text_to_number_binary(txt):
  txt = txt.lower()
  lis = txt.split(' ')
  out=[]
  if len(lis) >=8:
    for ele in lis:
      if ele == 'one':
        out.append('1')
      elif ele == 'zero':
        out.append('0')
    while len(out)%8 !=0:
      out.pop()
    return "".join(out) 
  
  return ""

