
def remove_special_characters(txt):
  return ''.join(filter(lambda x: x.isalnum() or x in " _-", txt))

