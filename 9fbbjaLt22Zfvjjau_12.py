
def paul_cipher(txt):
  c=0
  s=''
  letters='qazwsxedcrfvtgbyhnujmikolp'
  for l in txt.lower():
    if l in letters:
      s+=chr((ord(l)-ord('a')+c)%len(letters)+ord('a'))
      c=ord(l)-ord('a')+1
    else:
      s+=l
  return s.upper()

