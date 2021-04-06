
def validate_email(txt):
  return '' not in txt.split('@') and len(txt.split('@')[-1].split('.'))==2

