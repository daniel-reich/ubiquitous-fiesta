
def atbash(txt):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  ret = ''
  i = 0
  for char in txt:
    if char.isalpha():
      if char.isupper():
        ret = ret + alpha[-(alpha.index(char.lower())+1)].upper()
      else:
        ret = ret + alpha[-(alpha.index(char)+1)]
    else:
      ret = ret + char
  return ret

