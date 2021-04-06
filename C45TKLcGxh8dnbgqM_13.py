
def caesar_cipher(s, k):
  lowAlph = list("abcdefghijklmnopqrstuvwxyz")
  highAlph = list("abcdefghijklmnopqrstuvwxyz".upper())
  getInd = {}
  for i, c in enumerate(lowAlph):
    getInd[c] = i
  ret = ""
  for i in s:
    if i.islower():
      ind = getInd[i]
      ind = (ind+k)%26
      ret += lowAlph[ind]
    elif i.isupper():
      ind = getInd[i.lower()]
      ind = (ind+k)%26
      ret += highAlph[ind]
    else:
      ret += i
  return ret

