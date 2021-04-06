
def to_camel_case(txt):
  if txt == "": return ""
  txt2 = txt[0]
  txt = txt.title()
  for i in txt[1:]:
    if i.isalpha():
      txt2 += i
  return txt2

