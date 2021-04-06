
def get_missing_letters(s):
  
  alph = 'abcdefghijklmnopqrstuvwxyz'
  missing = ''
  
  for l8r in alph:
    if l8r not in s:
      missing += l8r
  
  return missing

