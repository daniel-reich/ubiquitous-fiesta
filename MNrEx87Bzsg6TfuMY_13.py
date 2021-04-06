
def create_id(firstname, lastname):
  return "{}{}".format(firstname[0].lower(), lastname[0:3].capitalize())

