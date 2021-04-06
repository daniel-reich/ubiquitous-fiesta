
import string
def keyword_cipher(key, message):
  b= []
  a = {}
  for i in key+string.ascii_lowercase:
    if i not in b:
      b.append(i)
  for i,j in enumerate(b):
    a[i] = j
  return ''.join(a[ord(i)-97] if i.isalpha() else i for i in message)

