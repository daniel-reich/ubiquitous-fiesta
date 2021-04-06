
def ascii_capitalize(txt):
  str1=''
  for i in txt:
    if ord(i)%2==0:
      str1+=i.upper()
    else:
      str1+=i.lower()
  return str1

