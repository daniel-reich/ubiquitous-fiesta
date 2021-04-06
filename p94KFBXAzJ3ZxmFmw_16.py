
def ascii_capitalize(txt):
  str=''
  for i in txt:
    if ord(i)%2==0:
      str+=i.upper()
    else:
      str+=i.lower()
  return str

