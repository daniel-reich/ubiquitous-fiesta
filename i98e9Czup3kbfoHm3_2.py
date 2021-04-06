
def text_to_number_binary(txt):
  l = []
  for i in txt.split():
    if i.lower() == "one" :
      l.append('1')
    elif i.lower() == 'zero' :
      l.append('0')
    else:
      None
  return "".join(l[:len(l)//8*8])

