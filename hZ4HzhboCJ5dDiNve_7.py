
def special_reverse_string(txt):
  v = [i for i in txt if i != ' '][::-1]
  s, j = '', 0
  for i in txt:
    if i == ' ':
      s = s + ' '
    else:
      if i.isupper():
        s = s + v[j].upper()
      elif i.islower():
        s = s + v[j].lower()
      else:
        s = s + v[j].lower()
      j = j + 1
  return s

