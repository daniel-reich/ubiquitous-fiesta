
def rolling_cipher(txt, n):
  txt_cipher = ''
  for char in txt:
    txt_cipher += chr((ord(char)-ord('a')+n)%26+ord('a'))
  return txt_cipher

