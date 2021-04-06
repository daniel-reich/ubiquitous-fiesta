
def keyword_cipher(key, message):
  k = ''
  for i in key:
    if i not in k:
      k+=i
  abc = 'abcdefghijklmnopqrstuvwxyz'
  for i in k:
    abc = abc.replace(i,'',1)
  new_abc = (k+abc)[:26]
  return ''.join(new_abc[ord(i)-97] if 0<=ord(i)-97<=26 else i for i in message)

