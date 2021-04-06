
def letters_only(txt):
  s = ''
  for i in txt:
    if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
      s += i
  return s

