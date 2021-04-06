
def remove_special_characters(txt):
  especial = '!@#$%^&\*()><.+=~|[]{},`?'
  s = ''
  for i in txt:
    if i not in especial:
      s += i
  
  return s

