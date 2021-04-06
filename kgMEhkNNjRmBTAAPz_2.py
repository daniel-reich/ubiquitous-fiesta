
def remove_special_characters(txt):
  return ''.join([t for t in txt if t.isalnum() or t in ' _-'])

