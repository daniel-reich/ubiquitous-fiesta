
def validate_email(txt):
  if "@" and "." in txt and txt.find("@") >= 1 and txt.rfind(".") > txt.find("@") + 1:
    return True
  else:
    return False

