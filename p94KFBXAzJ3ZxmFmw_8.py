
def ascii_capitalize(txt):
  ret = ""
  for i in range(len(txt)):
    if ord(txt[i]) % 2 == 0:
      ret += txt[i].upper()
    else:
      ret += txt[i].lower()
  return ret

