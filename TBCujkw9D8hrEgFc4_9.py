
def validate_email(txt):
  if '@' in txt and len(txt) > 0:
    if txt.index('@') > 0 and txt.count('@') == 1:
      if '.' in txt and txt.endswith('.com'):
        return True
        exit()
  return False

