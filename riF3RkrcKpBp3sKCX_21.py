
def cap_space(txt):
  result = ''
  for i in txt:
    if i.isupper() == True:
       result += ' '
    result += i.lower()
  return result

