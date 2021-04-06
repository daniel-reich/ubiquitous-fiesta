
def camelCasing(txt):
  txt = txt.lower()
  result = ""
  camel = False
  for i in txt:
    if i == " " or i == "_":
      camel = True
      continue
    if camel is False:
      result += i
    if camel is True:
      result += i.upper()
      camel = False
  return result

