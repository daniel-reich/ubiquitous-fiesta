
def create_id(firstname, lastname):
  if len(firstname) > 1 and len(lastname) > 3:
    return str(firstname[:1]).lower() + str(lastname[:1]).upper() + str(lastname[1:3]).lower()
  else:
    return str(firstname[:1]).lower() + str(lastname[:1]).upper() + str(lastname[1:3]).lower()

