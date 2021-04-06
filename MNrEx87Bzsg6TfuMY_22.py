
def create_id(firstname, lastname):
  
  LN = lastname[0:3].lower()
  return firstname[0].lower()+LN.capitalize()

