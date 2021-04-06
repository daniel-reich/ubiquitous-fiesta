
def baconify(msg, mask=None):
  import string
  d={'uuuuu' : 'a','uuuul' : 'b','uuulu' : 'c','uuull' : 'd','uuluu' : 'e','uulul' : 'f', 
  'uullu' : 'g', 'uulll' : 'h','uluuu' : 'i','uluul' : 'j','ululu' : 'k','ulull' : 'l',
  'ulluu' : 'm','ullul' : 'n','ulllu' : 'o','ullll' : 'p','luuuu' : 'q','luuul' : 'r',
  'luulu' : 's','luull' : 't','luluu' : 'u','lulul' : 'v','lullu' : 'w','lulll' : 'x',
  'lluuu' : 'y','lluul' : 'z','llllu' : '.','lllll' : ' '}
  str_c=''
  out=''
  if (mask==None):
    a= ''.join(msg.split())
    a=[i for i in a if i not in string.punctuation]
    letters=[a[i:i+5] for i in range(0,len(a),5) if len(a[i:i+5])==5]
    for letter in letters:
      for element in letter:
        if element == element.upper():
          str_c+='u'
        else:
          str_c+='l' 
      out+=d[str_c]
      str_c=''
    return (out)
  else:
    counter=0
    pattern=''
    for letter in msg:
      for key, value in d.items():  
        if value == letter.lower():
          pattern= key
          for p in pattern:
            if p=='u':
              while (mask[counter]==' ' or mask[counter] in string.punctuation):
                out+=mask[counter]
                counter+=1
              out+=mask[counter].upper()
              counter+=1
            else:
              while (mask[counter]==' ' or mask[counter] in string.punctuation):
                out+=mask[counter]
                counter+=1
              out+=mask[counter].lower()
              counter+=1
    while counter < len(mask):
      out+=mask[counter]
      counter+=1
    return(out)

