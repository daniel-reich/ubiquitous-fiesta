
def get_name(adr):
  return ''.join(i for i in adr.split('@')[0] if i.isalpha())

