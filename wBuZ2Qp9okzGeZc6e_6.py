
def first_place(road):
  if road:
    if [x for x in road if x.isalpha()]:
      return [x for x in road if x.isalpha()][-1]
    else:
      return None
  else:
    return None

