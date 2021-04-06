
def caesar_cipher(text, key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  alpha = alphabet*2
  res = ""
  for i in text:
    if i in alpha :
      res+= alpha[alpha.index(i)+key]
    else :
      res+=i
  return res

