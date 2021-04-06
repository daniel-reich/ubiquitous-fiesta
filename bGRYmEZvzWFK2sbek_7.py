
def get_missing_letters(s):
  alpha='abcdefghijklmnopqrstuvwxyz'
  t=''
  for x in alpha:
    if x not in s:
      t+=x
  return t

