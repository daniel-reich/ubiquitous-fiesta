
def is_valid_phone_number(txt):
  fb = txt[1:4]
  sb = txt[6:9]
  tb = txt[10:]
  if len(txt)==14:
    if txt[0]=="(" and txt[4]==")":
      if txt[5]==" " and txt[9]=="-":
        if fb.isdigit()==True and sb.isdigit()==True and tb.isdigit()==True:
          return True
  return False

