
def create_id(firstname, lastname):
  return '{}{}{}'.format(firstname[0].lower(), lastname[0].upper(), lastname[1:3].lower())

