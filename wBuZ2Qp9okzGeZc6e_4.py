
def first_place(road):
  return None if not road.replace("=", "").isalpha() else road.replace("=", "")[-1]

