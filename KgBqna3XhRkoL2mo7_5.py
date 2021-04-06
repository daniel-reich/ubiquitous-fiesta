
def decrypt(s):
  import string
  alphabet = string.ascii_lowercase
  mapping = {}
  num = 1
  for i in alphabet:
    mapping[num] = i
    num +=1
  print(mapping)
  
  idx = len(s)-1 
  decrypt = []
  while idx >=0:
    if s[idx] == '#':
      encode = s[idx-2:idx]
      idx += -3
    else:
      encode = s[idx]
      idx += -1
    decrypt.append(mapping[int(encode)])
  decrypt.reverse()
  return ''.join(decrypt)

