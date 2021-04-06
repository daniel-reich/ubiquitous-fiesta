
def paul_cipher(txt):
  txt1 = txt.upper()
  k = 'Z'
  x = ''
  for j in txt1:
    if j.isalpha():
      x += ''.join(chr(ord('A')+(ord(j)-ord('A')+ord(k)-ord('A')+1)%26))
      k = j
    else:
      x += j
  return x

