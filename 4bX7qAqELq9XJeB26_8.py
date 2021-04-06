
def to_camel_case(txt):
  camel = ''
  i = 0
  while i < len(txt):
    if txt[i] == '-' or txt[i] == '_':
      camel += txt[i+1].upper()
      i += 2
    else:
      camel += txt[i]
      i += 1
  return camel

