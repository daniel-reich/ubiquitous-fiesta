
def get_name(address):
  return ''.join([i for i in address.split('@')[0] if i.isalpha()])

