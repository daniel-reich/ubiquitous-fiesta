
def validate_email(txt):
  components = txt.split('@')
  return False if len(components) !=2 or len(components[0])<1 or '.' not in components[1] else True

