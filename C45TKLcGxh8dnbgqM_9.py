
def caesar_cipher(s, k):
  s,l=list(s),''
  if k>27:
    k=(k%27)+(k//27)
  for i in s:
    if i.isupper()==True:
      if (ord(i)+k) > 91: l=l+chr(64+(ord(i)+k)-90)
      else: l=l+chr(ord(i)+k)
    elif i.islower()==True:
      if (ord(i)+k) > 122: l=l+chr(96+((ord(i)+k)-122))
      else: l=l+chr(ord(i)+k)
    else: l=l+i
  return l

