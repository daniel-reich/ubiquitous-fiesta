
def rolling_cipher(txt, n):
  x=chr(ord(txt[0])+n)+chr(ord(txt[0])+n+1)+chr(ord(txt[0])+n+2)+chr(ord(txt[0])+n+3)
  for i in x:
    if ord(i)>ord('z'):
      x=x.replace(i, chr(ord(i)-26))
    if ord(i) < ord('a'):
      x = x.replace(i, chr(ord(i) + 26))
  return x

