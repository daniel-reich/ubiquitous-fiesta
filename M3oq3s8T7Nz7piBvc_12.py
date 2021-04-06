
def even_odd_string(txt):
 txt1 = ''
 txt2 = ''
 for i,x in enumerate(txt):
  if i % 2 == 0:
    txt1 += txt[i]
  else:
    txt2 += txt[i]
 return txt1 + ' ' + txt2

