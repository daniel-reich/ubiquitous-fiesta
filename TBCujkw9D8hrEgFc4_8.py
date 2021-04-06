
def validate_email(txt):
  if txt.find('@') == -1 or txt.find('.') == -1 or txt[0] == '@' or len(txt) == 0:
    return False
  if txt.find('@') > txt.rfind('.'):
    return False
  return True

