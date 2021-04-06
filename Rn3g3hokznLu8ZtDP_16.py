
def increment_string(txt):
  length_int = 0
  integer = 0
  for i in range(len(txt)):
    if 48 <= ord(txt[i]) <= 57:
      length_int = len(txt[i:])
      integer = int(txt[i:]) + 1
      txt = txt[:i]
      break
  if length_int == 0:
    txt += "1"
    return txt
  txt += ("0" * (length_int - len(str(integer)))) + str(integer)
  return txt

