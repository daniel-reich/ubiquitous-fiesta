
def validate_email(txt):
 if '@' in txt and '@' != txt[0] and '@' != txt[-1] and txt.count('@') == 1:
  i = txt.split("@")
  if i[0] != '.':
   if '.' in i[1] and i[1][0] != '.' and i[1][-1] != '.' :
    return True
   else:
    return False
  else:
   return False
 else:
  return False

