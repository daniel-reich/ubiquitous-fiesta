
def paul_cipher(txt):
  txt=txt.upper()
  P=[]
  res=''
  for x in txt:
    if x.isalpha():
      if not P:
        res+=x
        P.append(ord(x)-ord('A')+1)
      else:
        res+=chr(ord('A')+(ord(x)-ord('A')+1+P[-1])%26-1)
        P.append(ord(x)-ord('A')+1)
    else:
      res+=x
  return res

