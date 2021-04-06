
def first_place(road):
  if any(i.isalpha() for i in road) == True:
    return [i for i in road if i != "="][-1]
  else:
    return None

