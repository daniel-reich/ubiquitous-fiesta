
def letters_only(txt):
  a = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
  b = ''
  for x in txt:
    if x in a:
      b = b + x
  return b

