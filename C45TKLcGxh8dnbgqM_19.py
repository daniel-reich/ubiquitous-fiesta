
def caesar_cipher(s, k):
  a = "abcdefghijklmnopqrstuvwxyz"
  b = ""
  for i in s:
      if i.isalpha():
          if i.isupper():
              b += a[(a.index(i.lower())+k)%26].upper()
          else:
              b += a[(a.index(i)+k)%26]
      else: b += i
  return b

