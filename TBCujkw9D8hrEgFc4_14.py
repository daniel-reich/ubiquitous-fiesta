
def validate_email(txt):
  if (txt==''):
    return False  
  if ('@' in txt):
    name,domain = txt.split('@')
  else: return False
  if (len(name)>0 and '.com' in domain):
    return True
  else: 
    return False

