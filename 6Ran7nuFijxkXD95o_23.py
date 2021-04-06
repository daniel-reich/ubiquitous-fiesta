
def keyboard_shortcut(txt):
  data=txt
  clip=""
  c=1
  while c>=0 :
    c=data.find(' Ctrl + ')
    if c>=0:
      if (data[c+8]=='C'):
        clip=" " +data[:c]
        data=data[:c]+data[c+9:]
      else:
        if (data[c+8]=='V'):
          data=data[:c]+clip+data[c+9:]
  
  print(data)
  return data

