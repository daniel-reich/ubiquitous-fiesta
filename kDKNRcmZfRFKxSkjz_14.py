
def unmix(txt):
  txt1=''
  for i in range(0,len(txt),2):
    txt1+=(txt[i:i+2])[::-1]
  return txt1

