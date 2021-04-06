
def reverse_title(txt):
  str=""
  for x in txt.split():
    str+= x[0].lower()+x[1:].upper() + ' '
  return str[:-1]

