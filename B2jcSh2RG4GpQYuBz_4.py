
def is_valid_phone_number(txt):
  a=len(txt)
  if(a!=14):
    return False
  else:
    if(txt[0]!="(" or txt[4]!=")" or txt[5]!=" " or txt[9]!="-"):
      return False
  return True

