
def validate_email(txt):
  if '@' in txt[1:] and txt.endswith('.com'):
      return True
  return False

