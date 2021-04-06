
def first_place(road):
  return None if road==len(road)*'=' else [i for i in road if i.isalpha()][-1]

