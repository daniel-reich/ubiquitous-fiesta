
def validate_email(txt):
  return '@' in txt and '.' in txt and txt.rfind('.') > txt.rfind('@') and not txt.startswith('@')

